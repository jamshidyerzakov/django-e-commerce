import datetime
from django.utils.crypto import get_random_string


def unique_id_generator(instance):
    random_str = get_random_string()
    return f"{random_str}-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
