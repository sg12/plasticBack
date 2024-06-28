from rest_framework import permissions
from apps.user.models import Role
from .excepitons import IsNotClient


class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):        
        condition = request.user.role.name == Role.CLIENT
        if not condition:
            raise IsNotClient
        return True


class IsClientOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        condition = request.user.role.name == Role.CLIENT
        if not condition:
            raise IsNotClient
        return True
