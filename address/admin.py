from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import CustomerAddress, SellerAddress


@admin.register(CustomerAddress)
class CustomerAddressAdmin(TranslationAdmin):
    """Customer address"""
    list_display = ('address_line_1', 'address_line_2', 'country', 'state', 'city')


@admin.register(SellerAddress)
class CustomerAddressAdmin(TranslationAdmin):
    """Customer address"""
    list_display = ('address_line_1', 'address_line_2', 'country', 'state', 'city')
