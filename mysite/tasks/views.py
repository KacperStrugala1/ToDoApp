from django.shortcuts import render
from .models import Task

# Create your views here.
def task_view(request):
    #creating var that filter user model task 
    tasks = Task.objects.filter(user=request.user)
    return render(request,"tasks/tasks_page.html",{'model': tasks})
