from rest_framework import permissions
from apps.reception.models import Reception
from apps.user.models import User
from .exceptions import *


class HasReceptionOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user_pk = request.data.get('user')
        
        try:
            user = User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            raise UserDoesNotExist
        
        reception = Reception.objects.filter(
            doctor__pk=doctor_pk, 
            client=self.request.user
        ).first()
        
        if not reception:
            raise NoReception
        
        return True
