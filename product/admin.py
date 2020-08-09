from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Product, ProductImage


@admin.register(Product)
class CustomerAddressAdmin(TranslationAdmin):
    """Customer address"""
    list_display = ('title', 'description', 'product_fabricator')


admin.site.register(ProductImage)
