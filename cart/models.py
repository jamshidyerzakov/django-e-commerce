from django.db import models
from django.db.models.signals import m2m_changed
from djmoney.models.fields import MoneyField

from accounts.models import Customer

from.signals import m2m_changed_cart_receiver


class Cart(models.Model):
    customer = models.ForeignKey(
        'accounts.Customer',
        on_delete=models.PROTECT,
        verbose_name='Cart for customer',
        related_name='carts',
    )
    products = models.ManyToManyField(
        'product.Product',
        verbose_name='Products for the cart'
    )
    total = MoneyField(max_digits=12,
                       decimal_places=2,
                       default_currency='UZS',
                       default=0,
                       verbose_name='Total price of all products',
                       blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)
