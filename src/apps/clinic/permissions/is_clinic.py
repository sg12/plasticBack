from rest_framework import permissions
from apps.user.models import Role
from .excepitons import IsNotClinic


class IsClinic(permissions.BasePermission):
    def has_permission(self, request, view):
        condition = request.user.role.name == Role.CLINIC
        
        if not condition:
            raise IsNotClinic
        
        return True
