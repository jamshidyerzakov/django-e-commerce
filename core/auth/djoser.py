from django.db import IntegrityError, transaction
from djoser.conf import settings
from djoser.serializers import UserCreateSerializer

from service.accounts.general import create_user_by_type


class CustomUserCreateSerializer(UserCreateSerializer):
    """Rewriting the creation of user for djoser"""

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            # Todo: log this exception as critical while creating user
            self.fail("cannot_create_user")

        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = create_user_by_type(**validated_data)
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
        return user