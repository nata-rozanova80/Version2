
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),

    path('catalog/', include('catalog.urls')),  # Подключаем маршруты приложения catalog
    path('users/', include('users.urls')),  # Подключение пользователей
]


