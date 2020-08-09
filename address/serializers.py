from rest_framework import serializers
from django_countries.serializer_fields import CountryField

from .models import SellerAddress, CustomerAddress


class SellerAddressSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='selleraddress-detail')
    country = CountryField()

    class Meta:
        model = SellerAddress
        exclude = ('address_line_1', 'address_line_2', 'city', 'state')


class CustomerAddressSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='customeraddress-detail')
    country = CountryField()

    class Meta:
        model = CustomerAddress
        exclude = ('address_line_1', 'address_line_2', 'city', 'state')
