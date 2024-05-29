from rest_framework import permissions
from apps.user.models import Role


class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):        
        return request.user.role.name == Role.CLIENT


class IsClientOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user.role.name == Role.CLIENT
        )
            
