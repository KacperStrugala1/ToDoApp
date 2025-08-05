from django.urls import path

# importing views from views.py
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    
]