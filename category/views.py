from django_filters.rest_framework import DjangoFilterBackend

from service.general.views import CustomModelViewSet
from utils.serializers import get_serializer_by_action

from .models import Category
from .serializers import CategorySerializer, CategoryCreateSerializer


class CategoryViewSet(CustomModelViewSet):
    queryset = Category.objects.all()
    filter_backends = (DjangoFilterBackend,)
    lookup_field = 'slug'

    def get_serializer_class(self):
        """Specific serializer for specific action."""
        return get_serializer_by_action(
            action=self.action,
            serializers={
                'list': CategorySerializer,
                'retrieve': CategorySerializer,
                'create': CategoryCreateSerializer,
                'update': CategoryCreateSerializer,
                'partial_update': CategoryCreateSerializer,
                'metadata': CategorySerializer,
            }
        )

