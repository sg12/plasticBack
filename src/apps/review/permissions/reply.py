from rest_framework import permissions
from apps.review.models import *
from .exceptions import *


class IsAuthorProfile(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        review_pk = request.data.get('review')
        
        review = Review.objects.filter(pk=review_pk).first()
        if review:
            if review.user == request.user:
                return True
        
        raise IsNotAuthorProfile


class IsAuthorReply(permissions.BasePermission):
    def has_permission(self, request, view):
        pk = view.kwargs.get('pk')
        
        try:
            Reply.objects.get(pk=pk, author=request.user)
        except:
            raise IsNotAuthorReply
        
        return True
