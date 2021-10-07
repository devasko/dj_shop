from django.shortcuts import render


def shop(request):

    context = {'title': 'Магазин'}
    return render(request, 'shop/shop.html', context)


def cart(request):

    context = {'title': 'Корзина'}
    return render(request, 'shop/cart.html', context)


def checkout(request):

    context = {'title': 'Оформление'}
    return render(request, 'shop/checkout.html', context)

