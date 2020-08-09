from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Category


@admin.register(Category)
class CustomerAddressAdmin(TranslationAdmin):
    """Customer address"""
    list_display = ('title', 'description')
