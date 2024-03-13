from rest_framework import permissions

from django.contrib.auth import get_user_model


class IsRole(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        if request.user.is_superuser:
            return True
        else:
            return False


class IsEmptyRequest(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.data 