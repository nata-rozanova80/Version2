from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import register


urlpatterns = [
    path('', views.index),

    # Страница регистрации
    path('register/', register, name='register'),

    # Страница входа (используем стандартную форму Django)
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    # Страница выхода (используем стандартную Django-форму)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('register/', register, name='register'),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/', include('users.urls')),




]


