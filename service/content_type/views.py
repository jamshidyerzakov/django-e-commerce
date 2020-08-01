from django.contrib.contenttypes.models import ContentType
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from service.content_type.serializers import ContentTypeSerializer


class ContentTypeView(ListAPIView):
    serializer_class = ContentTypeSerializer
    queryset = ContentType.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
