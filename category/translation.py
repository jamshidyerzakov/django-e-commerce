from modeltranslation.translator import TranslationOptions, register

from .models import Category


@register(Category)
class CustomerAddressTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
