from service.accounts.general import create_user_by_type
from service.accounts.other import get_fields


def create_user(strategy, details, backend, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}
    print("USER:", "kwargs", kwargs, "args", args, "backend:", backend.__dict__, "details", details, "strategy:", strategy.__dict__, sep="\n\n")
    fields = get_fields(data=backend.data, **kwargs)

    print(fields)
    if not fields:
        return

    return {
        'is_new': True,
        'user': create_user_by_type(**fields)
    }
