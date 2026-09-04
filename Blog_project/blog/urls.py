from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_list, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('article/<int:article_id>', views.article, name='article'),
    path('create/', views.create_article, name='create'),
    path('edit/<int:article_id>', views.edit, name='edit'),
    path('delete/<int:article_id>', views.delete, name='delete')
]