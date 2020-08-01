from django.contrib.contenttypes.models import ContentType

from accounts import serializers


class ContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentType
        fields = '__all__'
