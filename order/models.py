from django.db import models
from django.db.models.signals import pre_save, post_save
from djmoney.models.fields import MoneyField

from cart.models import Cart
from .signals import pre_save_create_order_id, post_save_order


class Order(models.Model):
    class Status(models.TextChoices):
        CREATED = 'created'
        PAID = 'paid'
        DELIVERED = 'delivered'

    order_id = models.CharField(
        max_length=128,
        unique=True,
        blank=True,
        verbose_name="Automatically generated unique order id"
    )
    customer = models.ForeignKey(
        'accounts.Customer',
        on_delete=models.PROTECT,
        verbose_name="Order for a customer",
        related_name="customer_orders"
    )
    driver = models.ForeignKey(
        'accounts.Driver',
        on_delete=models.PROTECT,
        verbose_name="Driver for an order",
        related_name="driver_orders",
        blank=True,
        null=True,
    )
    seller = models.ForeignKey(
        'accounts.Seller',
        on_delete=models.PROTECT,
        verbose_name="Seller for an order",
        related_name="seller_orders",
        blank=True,
        null=True,
    )
    cart = models.ForeignKey(
        'cart.Cart',
        on_delete=models.PROTECT,
        verbose_name="Cart of the order",
    )
    total = MoneyField(
        max_digits=12,
        decimal_places=2,
        default_currency='UZS',
        default=0,
        verbose_name='Total price of an order',
        blank=True
    )
    status = models.CharField(
        max_length=64,
        choices=Status.choices,
        default=Status.CREATED,
        verbose_name="Status of an order"
    )

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order — {self.order_id}"

    class Meta:
        ordering = ['-created_at']


pre_save.connect(pre_save_create_order_id, sender=Order)
post_save.connect(post_save_order, sender=Order)
