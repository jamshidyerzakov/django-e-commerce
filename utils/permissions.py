from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """ Custom permission to check whether the user admin or not. """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_admin)


class IsOwnerOrAdmin(BasePermission):
    """ Custom permission to allow owners of an object or admins to edit it. """
    def has_object_permission(self, request, view, obj):
        return bool(bool(request.user == obj.user) or bool(request.user and request.user.is_admin))


class IsStaff(BasePermission):
    """ Custom permission to check whether user from staff or not. """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)
