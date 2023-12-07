""" Права доступа для приложения users """
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsOwnerOrReadOnly(permissions.BasePermission):
    """ Права доступа для владельцев или для чтения"""

    message = "У Вас не достаточно прав для доступа!"

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.id == view.get_object().id:
            return True
        return False


class IsOwner(permissions.BasePermission):
    """ Права доступа для владельцев """

    message = "У Вас не достаточно прав для доступа!"

    def has_permission(self, request, view):
        if request.user.id == view.get_object().id:
            return True
        return False

class IsOwnerOrStaff(permissions.BasePermission):
    """ Права доступа для владельцев или для суперпользователя"""

    message = "У Вас не достаточно прав для доступа!"

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.user.id == view.get_object().id:
            return True
        return False
