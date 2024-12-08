from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Order, OrderItem
from catalog.models import Product



@login_required
def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Сохраняем заказ без подтверждения
            order = form.save(commit=False)
            order.user = request.user  # Назначаем текущего пользователя
            order.save()

            # Получаем данные из корзины (примерный код)
            cart = request.session.get('cart', {})  # Ожидаем, что корзина хранится в сессии
            for product_id, quantity in cart.items():
                product = Product.objects.get(id=product_id)
                OrderItem.objects.create(order=order, product=product, quantity=quantity)

            # Очистка корзины
            request.session['cart'] = {}

            return redirect('order_success')  # Перенаправляем на страницу успешного оформления заказа
    else:
        form = OrderForm()

    return render(request, 'orders/place_order.html', {'form': form})


def order_success(request):
    return render(request, 'orders/order_success.html')
