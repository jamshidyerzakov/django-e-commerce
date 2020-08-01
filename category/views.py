from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from service.general.permissions import get_custom_permissions
from utils.serializers import get_serializer_by_action

from .models import Category
from .serializers import CategorySerializer, CategoryCreateSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    filter_backends = (DjangoFilterBackend,)
    lookup_field = 'slug'

    def get_permissions(self):
        """Specific permissions for specific HTTP query method."""
        self.permission_classes = get_custom_permissions(request=self.request)

        return super(CategoryViewSet, self).get_permissions()

    def get_serializer_class(self):
        """Specific serializer for specific action."""
        return get_serializer_by_action(
            action=self.action,
            serializers={
                'list': CategorySerializer,
                'retrieve': CategorySerializer,
                'create': CategoryCreateSerializer,
                'update': CategorySerializer,
                'partial_update': CategorySerializer,
                'metadata': CategorySerializer,
            }
        )

