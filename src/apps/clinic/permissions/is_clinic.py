from rest_framework import permissions
from apps.user.models import User, Role


class IsClinic(permissions.BasePermission):
    def has_permission(self, request, view):
        user = None
        user_pk = view.kwargs.get('user_pk')
        
        if user_pk:
            user = User.objects.get(pk=user_pk)
        else:
            user = request.user
        
        return user.role.name == Role.CLINIC
