from django_filters.rest_framework import DjangoFilterBackend

from service.general.views import CustomModelViewSet
from utils.serializers import get_serializer_by_action

from .models import Cart
from .serializers import (
    CartCreateSerializer,
    CartSerializer,
    CartUpdateSerializer
)


class CartViewSet(CustomModelViewSet):
    queryset = Cart.objects.all()
    filter_backends = (DjangoFilterBackend,)

    def get_serializer_class(self):
        """Specific serializer for specific action."""
        return get_serializer_by_action(
            action=self.action,
            serializers={
                'list': CartSerializer,
                'retrieve': CartSerializer,
                'create': CartCreateSerializer,
                'update': CartUpdateSerializer,
                'partial_update': CartUpdateSerializer,
                'metadata': CartSerializer,
            }
        )

