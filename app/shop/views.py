from django.shortcuts import render
from .models import *

# Главная страница магазина
def shop(request):
    products = Product.objects.all()
    context = {'title': 'Магазин', 'products': products}
    return render(request, 'shop/shop.html', context)


# Страница корзины
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'title': 'Корзина', 'items': items, 'order': order}
    return render(request, 'shop/cart.html', context)


# Страница охформления заказа
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'title': 'Оформление заказа', 'items': items, 'order': order}
    return render(request, 'shop/checkout.html', context)


