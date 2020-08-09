from modeltranslation.translator import register, TranslationOptions

from .models import (
    SellerAddress, CustomerAddress
)


@register(SellerAddress)
class SellerAddressTranslationOptions(TranslationOptions):
    fields = ('address_line_1', 'address_line_2', 'city', 'state')


@register(CustomerAddress)
class CustomerAddressTranslationOptions(TranslationOptions):
    fields = ('address_line_1', 'address_line_2', 'city', 'state')
