from rest_framework import viewsets

from service.general.permissions import get_custom_permissions

from accounts.models import User, Seller, Customer, Driver, Moderator, Admin
from accounts.serializers import (
    CustomUserSerializer,
    SellerSerializer,
    CustomerSerializer,
    DriverSerializer,
    ModeratorSerializer,
    AdminSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """ A ViewSet that provides CRUD for User object """
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        self.permission_classes = get_custom_permissions(request=self.request)

        return super(UserViewSet, self).get_permissions()


class SellerViewSet(viewsets.ModelViewSet):
    """ A ViewSet that provides CRUD for Seller object """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    def get_permissions(self):
        self.permission_classes = get_custom_permissions(request=self.request)

        return super(SellerViewSet, self).get_permissions()

    def perform_destroy(self, instance):
        instance.more.delete()
        instance.delete()


class CustomerViewSet(viewsets.ModelViewSet):
    """ A ViewSet that provides CRUD for Customer object """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_permissions(self):
        self.permission_classes = get_custom_permissions(request=self.request)

        return super(CustomerViewSet, self).get_permissions()

    def perform_destroy(self, instance):
        instance.more.delete()
        instance.delete()


class DriverViewSet(viewsets.ModelViewSet):
    """ A ViewSet that provides CRUD for Driver object """
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def get_permissions(self):
        self.permission_classes = get_custom_permissions(request=self.request)
        return super(DriverViewSet, self).get_permissions()

    def perform_destroy(self, instance):
        instance.more.delete()
        instance.delete()


class ModeratorViewSet(viewsets.ModelViewSet):
    """ A ViewSet that provides CRUD for Moderator object """
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer

    def get_permissions(self):
        self.permission_classes = get_custom_permissions(request=self.request)
        return super(ModeratorViewSet, self).get_permissions()

    def perform_destroy(self, instance):
        instance.more.delete()
        instance.delete()


class AdminViewSet(viewsets.ModelViewSet):
    """ A ViewSet that provides CRUD for Admin object """
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

    def get_permissions(self):
        self.permission_classes = get_custom_permissions(request=self.request)
        return super(AdminViewSet, self).get_permissions()

    def perform_destroy(self, instance):
        instance.more.delete()
        instance.delete()
