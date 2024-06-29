from rest_framework import permissions
from apps.support.models import Ticket
from .excepitons import IsNotAuthorTicket


class IsAuthorTicket(permissions.BasePermission):
    def has_permission(self, request, view):
        pk = view.kwargs.get('pk')
        
        try:
            Ticket.objects.get(pk=pk, author=request.user)
        except Ticket.DoesNotExist:
            raise IsNotAuthorTicket
        
        return True
