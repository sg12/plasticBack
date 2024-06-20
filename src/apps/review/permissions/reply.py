from rest_framework import permissions
from apps.review.models import *
from .exceptions import *


class IsAuthorProfile(permissions.BasePermission):
    'Делает проверку, чтобы профиль мог отвечать только на отзывы из своего профиля'
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        review_pk = request.data.get('review')
        
        review = Review.objects.filter(pk=review_pk, user=request.user).first()
        if review:
            return True
        
        raise IsNotAuthorProfile


class IsAuthorReply(permissions.BasePermission):
    'Является ли pk пользователя из URL автором ответа на отзыв'
    
    def has_permission(self, request, view):
        pk = view.kwargs.get('pk')
        
        try:
            Reply.objects.get(pk=pk, author=request.user)
        except:
            raise IsNotAuthorReply
        
        return True
