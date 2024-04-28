from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings


# Create your models here.
class Article(models.Model):
    category_choices = [
        ('option1', '취미'),
        ('option2', '음식'),
        ('option3', '프로그래밍'),]
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50, choices=category_choices, default='option1')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articles', null=True)
    last_read_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    last_read_time = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments' ,null=True)
    
    def __str__(self):
        return self.content[:20]
    
class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create_user(self, username, password):
        if not username:
            raise ValueError('you must have username, idiot')
        if not password:
            raise ValueError('you must have password, idiot')
    
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
        
    
    
    
class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    
    username = models.CharField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    
    def __str__(self) -> str:
        return self.username
    


