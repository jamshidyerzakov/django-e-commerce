from rest_framework import serializers

from .models import SellerAddress, CustomerAddress


class SellerAddressSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='selleraddress-detail')

    class Meta:
        model = SellerAddress
        fields = '__all__'


class CustomerAddressSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='customeraddress-detail')

    class Meta:
        model = CustomerAddress
        fields = '__all__'
