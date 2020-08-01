from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    BasePermission,
    AllowAny,
)

from utils.permissions import IsOwnerOrAdmin, IsStaff
from utils.http_methods import METHODS
from utils.exceptions import BadHTTPMethodError

_DEFAULT_PERMISSIONS = {
    'GET': (AllowAny,),  # (IsAuthenticatedOrReadOnly,),
    'POST': (AllowAny,),  # (IsAuthenticated,),
    'PUT': (AllowAny,),  # (IsAuthenticated, IsOwnerOrAdmin),
    'PATCH': (AllowAny,),  # (IsAuthenticated, IsOwnerOrAdmin),
    'DELETE': (AllowAny,),  # (IsAuthenticated, IsStaff,),
}


def get_custom_permissions(request, **extra_permissions):
    """
    Returning tuple of permissions for each HTTP method accordingly

    :param request: in order to get HTTP method
    :param extra_permissions: expecting {HTTP method : (permissions, )}, _DEFAULT_PERMISSIONS can be rewritten
    :return: tuple of permissions or permission
    """

    if extra_permissions:
        for method, permissions in extra_permissions.items():

            for permission in permissions:
                if not isinstance(permission, BasePermission):
                    raise TypeError(f"TypeError: unexpected type of permission '{permission}'")

            if method not in METHODS:
                raise BadHTTPMethodError(f"BadHTTPMethodError: unexpected HTTP method '{method}'")

            _DEFAULT_PERMISSIONS[method] = permissions

    permissions = (
        permission
        for method, permissions in _DEFAULT_PERMISSIONS.items()
        for permission in permissions
        if request.method == method
    )

    return permissions
