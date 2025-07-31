from django.http import JsonResponse
from django.shortcuts import render
from tasks.models import Task
<<<<<<< HEAD
from django.views import View
import logging




class HomeView(View):
    def get(self, request):

        return render(request,"mysite/home.html")

class AboutView(View):
    
    def get(self, request):
        
        response_date = {"error": "about site"}
        logging.info("info function is working")
        return JsonResponse(response_date)
        
=======

def home_view(request):
    
    #{'tasks'is ta variable used in html}
    return render(request,"mysite/home.html")

def about_view(request):
    
    return HttpResponse("about site")
>>>>>>> kstrugala
