from rest_framework import serializers
from generic_relations.relations import GenericRelatedField
from rest_framework.exceptions import ValidationError

from accounts.models import Seller, Moderator, Admin
from category.models import Category
from service.product.content_type import get_product_creators, get_object_ids
from .models import Product


class SellerDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="accounts:seller-detail")

    class Meta:
        model = Seller
        fields = ('id', 'url', 'type', 'username')


class ModeratorDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="accounts:moderator-detail")

    class Meta:
        model = Moderator
        fields = ('id', 'url', 'type', 'username')


class AdminDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="accounts:admin-detail")

    class Meta:
        model = Admin
        fields = ('id', 'url', 'type', 'username')


class CategoryDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="category-detail", lookup_field="slug")

    class Meta:
        model = Category
        fields = ('id', 'url')


class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field="slug")
    category = CategoryDetailSerializer()
    owner = GenericRelatedField({
        Seller: SellerDetailSerializer(),
        Moderator: ModeratorDetailSerializer(),
        Admin: AdminDetailSerializer()
    })

    class Meta:
        model = Product
        exclude = ('slug', 'content_type', 'object_id', 'title', 'description', 'product_fabricator')


class ProductCreateSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field="slug")

    class Meta:
        model = Product
        exclude = ('slug', 'title', 'description', 'product_fabricator')

    def validate_content_type(self, value):
        if value.id not in get_product_creators():
            raise ValidationError(f"Bad content_type, possible values -> {list(get_product_creators().keys())}")
        return value

    def validate_object_id(self, value):
        content_type_id = self.initial_data['content_type']
        user_model_ids = get_object_ids(content_type_id)

        if value not in user_model_ids:
            raise ValidationError(f"Bad object id, possible values -> {user_model_ids}")
        return value


