from django.urls import path
from api import views

urlpatterns = [
    path('task_lists/', views.task_lists),
    path('task_lists/<int:pk>/', views.tasklist_detail),
    path('task_lists/<int:pk>/tasks/', views.tasklist_tasks),
    path('tasks/<int:pk>/', views.task_detail)
]
