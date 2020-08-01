from rest_framework import viewsets

from service.general.permissions import get_custom_permissions

from .models import SellerAddress, CustomerAddress
from .serializers import SellerAddressSerializer, CustomerAddressSerializer


class SellerAddressViewSet(viewsets.ModelViewSet):
    queryset = SellerAddress.objects.all()
    serializer_class = SellerAddressSerializer

    def get_permissions(self):
        self.permission_classes = get_custom_permissions(request=self.request)

        return super(SellerAddressViewSet, self).get_permissions()


class CustomerAddressViewSet(viewsets.ModelViewSet):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer

    def get_permissions(self):
        self.permission_classes = get_custom_permissions(request=self.request)

        return super(CustomerAddressViewSet, self).get_permissions()
