from modeltranslation.translator import TranslationOptions, register

from .models import Product


@register(Product)
class CustomerAddressTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'product_fabricator')
