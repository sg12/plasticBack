from rest_framework import permissions
from apps.user.models import Role
from .excepitons import IsNotDoctor


class IsDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        condition = request.user.role.name == Role.DOCTOR
        
        if not condition:
            raise IsNotDoctor
        
        return True
