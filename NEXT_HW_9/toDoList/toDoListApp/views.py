from django.shortcuts import render, redirect
from .models import Task
from django.utils.timezone import now
# Create your views here.
def home(request):
    tasks = Task.objects.all()
    for task in tasks:
        days_left = (task.deadline.date() - now().date()).days
        task.days_left = days_left

    tasks = sorted(tasks, key=lambda x: x.days_left)
    return render(request, 'home.html', {'tasks': tasks})

def taskToggle(request, id):
    task = Task.objects.get(pk=id)
    task.completed = not task.completed
    task.save()
    return redirect('home')

def new(request):
    categories = ['작업', '개인적인', '위시리스트']
    
    if request.method == 'POST':
        task = Task()
        task.title = request.POST['title']
        task.content = request.POST['content']
        task.category = request.POST['category']
        task.deadline = request.POST['deadline']
        task.save()
        return redirect('home')
    return render(request, 'new.html', {'categories': categories})

def detail(request, id):
    categories = ['작업', '개인적인', '위시리스트']
    task = Task.objects.get(pk=id)
    return render(request, 'detail.html', {'task': task, 'categories': categories})

def update(request, id):
    task = Task.objects.get(pk=id)
    categories = ['작업', '개인적인', '위시리스트']
    if request.method == 'POST':
        task.title = request.POST['title']
        task.content = request.POST['content']
        task.category = request.POST['category']
        task.deadline = request.POST['deadline']
        task.save()
        return redirect('detail', task.id)
    return render(request, 'update.html' , {'task': task, 'categories': categories})

def delete(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('home')