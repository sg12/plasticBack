from rest_framework import permissions
from apps.support.models import Message
from .excepitons import IsNotAuthorMsg


class IsAuthorMessage(permissions.BasePermission):
    def has_permission(self, request, view):
        pk = view.kwargs.get('pk')
        
        try:
            Message.objects.get(pk=pk, author=request.user)
        except Message.DoesNotExist:
            raise IsNotAuthorMsg
        
        return True
