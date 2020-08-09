from django.contrib.contenttypes.models import ContentType
from rest_framework.exceptions import ValidationError

from accounts.models import Admin, Moderator, Seller

_CREATOR_MODELS = {
    'admin': Admin,
    'moderator': Moderator,
    'seller': Seller
}


def get_object_ids(content_type_id):
    if int(content_type_id) not in list(get_product_creators()):
        raise ValidationError("Bad content_type")
    user_model = get_product_creators()[int(content_type_id)]
    queryset = user_model.objects.all()
    return [obj.id for obj in queryset]


def get_product_creators():
    possible_product_creators = {obj.id: _CREATOR_MODELS[obj.model] for obj in ContentType.objects.all() if
                                 obj.model in _CREATOR_MODELS}

    return possible_product_creators
