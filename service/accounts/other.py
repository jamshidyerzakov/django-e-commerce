USER_FIELDS = ['username', 'email']


def get_username_from_email(email):
    return email.split("@")[0]


def get_fields(data, **kwargs):
    fields = {name: value for name, value in kwargs['response'].items() if name in USER_FIELDS}
    fields['type'] = data.get('type', None)

    fields.setdefault('type', 'customer')
    fields.setdefault('username', get_username_from_email(kwargs['response']['email']))

    fields['first_name'] = kwargs['response'].get('name', '')
    fields['last_name'] = kwargs['response'].get('given_name', '')

    return fields