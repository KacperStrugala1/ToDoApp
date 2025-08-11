from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def task_view(request):
    #creating var that filter user model task 
    tasks = Task.objects.filter(user=request.user)
    return render(request,"tasks/tasks_page.html",{'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  
            task.save()
            return redirect('/task/') 
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})
