from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('chat/', views.chat, name='chat'),
    path('edit/<int:message_id>', views.edit, name='edit'),
    path('delete/<int:message_id>', views.delete, name='delete')
]