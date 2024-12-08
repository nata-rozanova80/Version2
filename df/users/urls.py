from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    # Регистрация
    path('register/', register, name='register'),
    # Вход (используем стандартное представление Django)
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # Выход (используем стандартное представление Django)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
