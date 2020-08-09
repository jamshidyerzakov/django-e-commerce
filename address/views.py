from service.general.views import CustomModelViewSet

from .models import SellerAddress, CustomerAddress
from .serializers import SellerAddressSerializer, CustomerAddressSerializer


class SellerAddressViewSet(CustomModelViewSet):
    queryset = SellerAddress.objects.all()
    serializer_class = SellerAddressSerializer


class CustomerAddressViewSet(CustomModelViewSet):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer
