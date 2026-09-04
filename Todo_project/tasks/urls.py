from django.urls import path

from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('edit/<int:id>/', views.task_edit, name='task_edit'),
    path('delete/<int:id>/', views.task_delete, name='task_delete'),
]