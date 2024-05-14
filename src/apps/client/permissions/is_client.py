from rest_framework import permissions
from apps.user.models import Role


class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):        
        return request.user.role.name == Role.CLIENT
            
