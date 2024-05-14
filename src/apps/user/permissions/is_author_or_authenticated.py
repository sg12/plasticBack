from rest_framework import permissions


class IsAuthorOrAuthenticated(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)

        return obj.author == request.user
