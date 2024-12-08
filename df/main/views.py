
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegisterForm


def index(request):
    #return HttpResponse("<h1>Это мой первый проект на Django</h1>")
    return render(request, 'index.html')  # путь к шаблону главной страницы


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт для {username} успешно создан!')
            login(request, user)  # Автоматически выполняем вход после регистрации
            return redirect('index')  # Перенаправление на главную
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
