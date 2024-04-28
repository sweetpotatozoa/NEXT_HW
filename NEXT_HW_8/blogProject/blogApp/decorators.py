from django.shortcuts import render, get_object_or_404
from functools import wraps
from django.utils import timezone


def is_owner_or_admin(request, obj):
    return obj.creator == request.user or request.user.is_superuser

def check_is_owner_or_admin(model_cls, lookup_field='id'):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            obj_id = kwargs.get(lookup_field)
            if not obj_id:
                return render(request, 'error.html', {'error': 'Object Id is not found.'})
            
            obj = get_object_or_404(model_cls, **{'id' : obj_id})
            
            if not is_owner_or_admin(request, obj):
                return render(request, 'error.html', {'error': 'Permission Denied.'})
            return view_func(request, *args, **kwargs)
        
        return _wrapped_view
    return decorator

            
def update_last_read(func):
    @wraps(func)
    def wrapper(request, *arg, **kwargs):
        response = func(request, *arg, **kwargs)
        article_id = kwargs.get('article_id')
        if article_id:
            from .models import Article
            article = Article.objects.get(id=article_id)
            article.last_read_by = request.user
            article.last_read_time = timezone.now()
            article.save()
        return response
    return wrapper