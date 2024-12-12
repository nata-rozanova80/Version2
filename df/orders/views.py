# orders/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OrderForm
from .models import Order, OrderItem
from catalog.models import Product

@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.warning(request, "Ваша корзина пуста! Добавьте товары, прежде чем оформлять заказ.")
        return redirect('product_list')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            # Добавляем товары из корзины в заказ
            for product_id, quantity in cart.items():
                product = Product.objects.get(id=product_id)
                OrderItem.objects.create(order=order, product=product, quantity=quantity)

            # Очищаем корзину
            request.session['cart'] = {}

            messages.success(request, "Заказ успешно оформлен! Мы свяжемся с вами для подтверждения.")
            return redirect('product_list')
    else:
        form = OrderForm()

    return render(request, 'orders/checkout.html', {'form': form})
