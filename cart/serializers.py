from rest_framework import serializers

from product.models import Product
from .models import Cart
from accounts.models import Customer


class CustomerDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='accounts:customer-detail')

    class Meta:
        model = Customer
        fields = ('id', 'url', 'username', 'type')


class ProductDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='slug')

    class Meta:
        ref_name = 'Product 1'
        model = Product
        fields = ('id', 'url', 'product_fabricator')


class CartCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        exclude = ('total',)


class CartUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    customer = CustomerDetailSerializer()
    products = ProductDetailSerializer(many=True)
    url = serializers.HyperlinkedIdentityField(view_name='cart-detail')

    class Meta:
        model = Cart
        fields = '__all__'
