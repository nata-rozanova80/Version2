from django.urls import path
from .views import product_list
from .views import view_cart
from .views import index

urlpatterns = [
    path('', index, name='index'),  # Главная страница
    path('products/', product_list, name='product_list'),

# Другие маршруты...
    path('cart/', view_cart, name='view_cart'),
]



