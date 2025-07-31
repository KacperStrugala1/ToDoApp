from django.urls import path

# importing views from views.py
from . import views

urlpatterns = [
    path('', views.task_view, name="tasks"),
<<<<<<< HEAD
    path('add/',views.create_task, name = "create_task"),
=======
>>>>>>> kstrugala
]