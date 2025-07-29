from django.http import HttpResponse
from django.shortcuts import render
from tasks.models import Task

def home_view(request):
    
    #{'tasks'is ta variable used in html}
    return render(request,"mysite/home.html")

def about_view(request):
    
    return HttpResponse("about site")