from django.urls import path
from .views import place_order
from .views import order_success

urlpatterns = [
    path('place-order/', place_order, name='place_order'),
]

urlpatterns += [
    path('order-success/', order_success, name='order_success'),
]
