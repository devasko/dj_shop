from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    login = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Product(models.Model):
    title = models.CharField(max_length=150, null=True, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    digital = models.BooleanField(default=False, null=True, blank=False, verbose_name='Цифровой продукт')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    @property
    def imgURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Покупатель')
    date_ordered = models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки')
    complete = models.BooleanField(default=False, null=True, blank=False, verbose_name='Завершен')
    transaction_id = models.CharField(max_length=100, null=True, verbose_name='Транзакция')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Товар')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Заказ')
    quantity = models.IntegerField(default=0, blank=True, null=True, verbose_name='Количество')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки')

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    index = models.CharField(max_length=50, null=False)
    region = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    recipient = models.CharField(max_length=200, null=False)
    note = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
