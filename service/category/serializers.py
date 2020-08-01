from rest_framework import serializers


class FilterCategorySerializer(serializers.ListSerializer):
    """Filtering categories, only parents"""

    def to_representation(self, categories):
        if isinstance(categories, list):
            return super().to_representation([category for category in categories if not category.children_categories])
        return super().to_representation(categories.filter(children_categories=None))
