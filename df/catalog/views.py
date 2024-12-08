from django.shortcuts import render
from .models import Product
from catalog.models import Product


from django.shortcuts import redirect
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})



def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    messages.success(request, 'Товар добавлен в корзину!')
    return redirect('product_list')


#Просмотр корзины должен стоять после других представлений

def view_cart(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            products.append({'product': product, 'quantity': quantity})
            total += product.price * quantity
        except Product.DoesNotExist:
            continue  # Игнорируем товары, которые удалены из базы

    return render(request, 'catalog/view_cart.html', {'products': products, 'total': total})
