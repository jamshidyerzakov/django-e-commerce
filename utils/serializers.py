from typing import Dict
from rest_framework.serializers import Serializer

# ACTIONS = ['list', 'retrieve', 'create', 'update', 'partial_update', 'metadata']


def get_serializer_by_action(action: str, serializers: Dict[str, type(Serializer)]):
    """
    Returning serializer according to action of HTTP request

    :param action: HTTP request action
    :param serializers: expecting dict object => {action_name : serializer}
    :return: serializer object
    """

    for current_action, serializer in serializers.items():
        if action == current_action:
            return serializer
