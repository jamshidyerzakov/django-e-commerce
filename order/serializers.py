from rest_framework import serializers

from cart.serializers import CustomerDetailSerializer
from cart.models import Cart
from accounts.models import Driver
from .models import Order


class DriverDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="accounts:driver-detail")

    class Meta:
        model = Driver
        fields = ('id', 'type', 'url', 'username')


class CartDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="cart-detail")

    class Meta:
        model = Cart
        fields = ('id', 'url')


class OrderUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        exclude = ('order_id',)


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('total', 'order_id')


class OrderDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='order-detail', lookup_field='order_id')

    class Meta:
        model = Order
        fields = ('order_id', 'url', 'total', 'total_currency')


class OrderSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='order-detail', lookup_field='order_id')
    driver = DriverDetailSerializer()
    customer = CustomerDetailSerializer()
    cart = CartDetailSerializer()

    class Meta:
        model = Order
        fields = '__all__'
