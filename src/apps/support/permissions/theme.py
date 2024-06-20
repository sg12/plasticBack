from rest_framework import permissions
from apps.support.models import Theme


class IsAuthorTheme(permissions.BasePermission):
    def has_permission(self, request, view):
        pk = view.kwargs.get('pk') # theme id
        theme = Theme.objects.filter(
            pk=pk,
            author=request.user
        ).first()
        
        return bool(theme)
