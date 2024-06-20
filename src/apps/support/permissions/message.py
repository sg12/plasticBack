from rest_framework import permissions
from apps.support.models import Message


class IsAuthorMessage(permissions.BasePermission):
    def has_permission(self, request, view):
        pk = view.kwargs.get('pk') # message id
        msg = Message.objects.filter(
            pk=pk,
            author=request.user
        ).first()
        
        return bool(msg)
