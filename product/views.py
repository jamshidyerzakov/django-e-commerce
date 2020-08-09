from rest_framework.viewsets import ModelViewSet

from service.general.permissions import get_custom_permissions
from utils.serializers import get_serializer_by_action
from .serializers import ProductSerializer, ProductCreateSerializer
from .models import Product


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    lookup_field = 'slug'

    def get_permissions(self):
        self.permission_classes = get_custom_permissions(request=self.request)

        return super(ProductViewSet, self).get_permissions()
    
    def get_serializer_class(self):
        """Specific serializer for specific action."""
        return get_serializer_by_action(
            action=self.action,
            serializers={
                'list': ProductSerializer,
                'retrieve': ProductSerializer,
                'create': ProductCreateSerializer,
                'update': ProductCreateSerializer,
                'partial_update': ProductCreateSerializer,
                'metadata': ProductSerializer
            }
        )



