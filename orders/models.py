from django.db import models
from shop.models import Product
from account.models import Profile


class Delivery(models.Model):
    d_type = models.CharField(max_length=50)
    d_price = models.CharField(max_length=50)

    def __str__(self):
        return self.d_type


class Payment(models.Model):
    p_type = models.CharField(max_length=50)

    def __str__(self):
        return self.p_type


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='E-mail')
    city = models.CharField(max_length=50, verbose_name='Город')
    status = models.CharField(max_length=50, default=1, verbose_name='Статус')
    address = models.CharField(max_length=50, verbose_name='Адрес')
    ord_check_time = models.DateTimeField(null=True, verbose_name='Дата доставки')
    price = models.ForeignKey(Product, default=1, on_delete=models.CASCADE)
    p_type = models.ForeignKey(Payment, default=1, on_delete=models.CASCADE)
    d_type = models.ForeignKey(Delivery, default=1, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False, verbose_name='Оплачено')
    created = models.DateTimeField(auto_now_add=True)
    # braintree_id = models.CharField(max_length=150, blank=True)
    # updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.paid)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              default=1, related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, default=1, related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

