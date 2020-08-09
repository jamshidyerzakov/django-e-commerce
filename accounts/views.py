from django.db.models.deletion import ProtectedError
from rest_framework.exceptions import ValidationError

from service.general.views import CustomModelViewSet

from .models import User, Seller, Customer, Driver, Moderator, Admin
from .serializers import (
    CustomUserSerializer,
    SellerSerializer, SellerCreateSerializer,
    CustomerSerializer, CustomerCreateSerializer,
    DriverSerializer, DriverCreateSerializer,
    ModeratorSerializer, ModeratorCreateSerializer,
    AdminSerializer, AdminCreateSerializer
)
from utils.serializers import get_serializer_by_action


class UserViewSet(CustomModelViewSet):
    """ A ViewSet that provides CRUD for User object """
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

    def perform_destroy(self, instance):
        try:
            instance.delete()
        except ProtectedError:
            raise ValidationError({
                "Details": "Cannot delete user with 'more' field. Delete this user from its corresponding API"
            })



class SellerViewSet(CustomModelViewSet):
    """ A ViewSet that provides CRUD for Seller object """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    def get_serializer_class(self):
        """Specific serializer for specific action."""
        return get_serializer_by_action(
            action=self.action,
            serializers={
                'list': SellerSerializer,
                'retrieve': SellerSerializer,
                'create': SellerCreateSerializer,
                'update': SellerCreateSerializer,
                'partial_update': SellerCreateSerializer,
                'metadata': SellerSerializer,
            }
        )

    def perform_destroy(self, instance):
        instance.more.delete()
        instance.delete()


class CustomerViewSet(CustomModelViewSet):
    """ A ViewSet that provides CRUD for Customer object """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_serializer_class(self):
        """Specific serializer for specific action."""
        return get_serializer_by_action(
            action=self.action,
            serializers={
                'list': CustomerSerializer,
                'retrieve': CustomerSerializer,
                'create': CustomerCreateSerializer,
                'update': CustomerCreateSerializer,
                'partial_update': CustomerCreateSerializer,
                'metadata': CustomerSerializer,
            }
        )

    def perform_destroy(self, instance):
        instance.more.delete()
        instance.delete()


class DriverViewSet(CustomModelViewSet):
    """ A ViewSet that provides CRUD for Driver object """
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def get_serializer_class(self):
        """Specific serializer for specific action."""
        return get_serializer_by_action(
            action=self.action,
            serializers={
                'list': DriverSerializer,
                'retrieve': DriverSerializer,
                'create': DriverCreateSerializer,
                'update': DriverCreateSerializer,
                'partial_update': DriverCreateSerializer,
                'metadata': DriverSerializer,
            }
        )

    def perform_destroy(self, instance):
        instance.more.delete()
        instance.delete()


class ModeratorViewSet(CustomModelViewSet):
    """ A ViewSet that provides CRUD for Moderator object """
    queryset = Moderator.objects.all()
    serializer_class = ModeratorSerializer

    def get_serializer_class(self):
        """Specific serializer for specific action."""
        return get_serializer_by_action(
            action=self.action,
            serializers={
                'list': ModeratorSerializer,
                'retrieve': ModeratorSerializer,
                'create': ModeratorCreateSerializer,
                'update': ModeratorCreateSerializer,
                'partial_update': ModeratorCreateSerializer,
                'metadata': ModeratorSerializer,
            }
        )

    def perform_destroy(self, instance):
        instance.more.delete()
        instance.delete()


class AdminViewSet(CustomModelViewSet):
    """ A ViewSet that provides CRUD for Admin object """
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

    def get_serializer_class(self):
        """Specific serializer for specific action."""
        return get_serializer_by_action(
            action=self.action,
            serializers={
                'list': AdminSerializer,
                'retrieve': AdminSerializer,
                'create': AdminCreateSerializer,
                'update': AdminCreateSerializer,
                'partial_update': AdminCreateSerializer,
                'metadata': AdminSerializer,
            }
        )

    def perform_destroy(self, instance):
        instance.more.delete()
        instance.delete()





