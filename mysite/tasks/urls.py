from django.urls import path

# importing views from views.py
from . import views

urlpatterns = [
    path('', views.task_view, name="tasks"),
    path('add/',views.create_task, name = "create_task"),
]