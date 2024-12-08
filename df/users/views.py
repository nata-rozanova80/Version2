# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm  # Предполагается, что вы создали эту форму

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)    # Автоматически авторизуем пользователя
            return redirect('index')  # Перенаправляем на главную страницу после регистрации
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



# Что делает данный код:
# Наследование от UserCreationForm:
# UserCreationForm — встроенная форма Django для регистрации пользователей, которая автоматически
# проверяет пароли и их подтверждение.
#
# Добавление поля email:
# Поле email не является обязательным во встроенной модели User, поэтому мы явно добавляем его
# в форму и отмечаем как обязательное (required=True).
#
# Класс Meta: Включает поля username, email, password1 и password2. Эти поля используются
# для сбора информации от пользователя. Django автоматически применит все необходимые
# валидации для пароля.
