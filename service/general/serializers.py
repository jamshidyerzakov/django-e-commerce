from rest_framework import serializers


class RecursiveSerializer(serializers.Serializer):
    """Recursive display of children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data