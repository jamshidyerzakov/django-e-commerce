from rest_framework import viewsets

from service.general.permissions import get_custom_permissions


class CustomModelViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        self.permission_classes = get_custom_permissions(request=self.request)
        return super().get_permissions()
