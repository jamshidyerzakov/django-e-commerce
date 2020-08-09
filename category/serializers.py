from rest_framework import serializers

from product.models import Product
from service.category.serializers import FilterCategorySerializer
from service.general.serializers import RecursiveSerializer

from .models import Category


class ProductDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field="slug")

    class Meta:
        model = Product
        fields = ('id', 'url')


class CategoryCreateSerializer(serializers.ModelSerializer):
    """General serializer for the Category model"""

    class Meta:
        model = Category
        exclude = ('slug', 'title', 'description')


class CategorySerializer(serializers.ModelSerializer):
    """Detail serializer for the Category model"""
    url = serializers.HyperlinkedIdentityField(view_name="category-detail", lookup_field="slug")
    children = RecursiveSerializer(many=True)
    products = ProductDetailSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCategorySerializer
        model = Category
        exclude = ('parent_category', 'slug', 'title', 'description')

