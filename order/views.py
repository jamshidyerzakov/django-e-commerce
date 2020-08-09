from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from service.general.permissions import get_custom_permissions
from utils.serializers import get_serializer_by_action

from .models import Order
from .serializers import (
    OrderCreateSerializer,
    OrderSerializer,
    OrderUpdateSerializer
)


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    filter_backends = (DjangoFilterBackend,)
    lookup_field = 'order_id'

    def get_permissions(self):
        """Specific permissions for specific HTTP query method."""
        self.permission_classes = get_custom_permissions(request=self.request)

        return super(OrderViewSet, self).get_permissions()

    def get_serializer_class(self):
        """Specific serializer for specific action."""
        return get_serializer_by_action(
            action=self.action,
            serializers={
                'list': OrderSerializer,
                'retrieve': OrderSerializer,
                'create': OrderCreateSerializer,
                'update': OrderUpdateSerializer,
                'partial_update': OrderUpdateSerializer,
                'metadata': OrderSerializer,
            }
        )
