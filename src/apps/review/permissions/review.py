from rest_framework import permissions
from apps.reception.models import Reception
from apps.user.models import User
from apps.review.models import *
from .exceptions import *


class IsAuthorReview(permissions.BasePermission):
    '''
    Является ли пользовтель автором отзыва.
    Рабочие методы: `PATCH`, `DELETE`.
    '''
    
    def has_permission(self, request, view):
        if request.method != 'PATCH' and request.method != 'DELETE':
            return True
        
        user_pk = view.kwargs.get('pk')
        
        review = Review.objects.filter(
            user__pk=user_pk, 
            author=request.user
        ).first()
        
        if review:
            return True
        
        raise IsNotAuthorReview


class OnlyOneReview(permissions.BasePermission):
    '''
    Если еще нет отзыва, пользователь имеет право его оставить.
    Рабочий метод: `POST`.
    '''
    
    def has_permission(self, request, view):
        if request.method != 'POST':
            return True
        
        pk = view.kwargs.get('pk')
        user = User.objects.get(pk=pk)
        
        count = Review.objects.filter(
            author=request.user,
            user=user,
        ).count()
        
        if count > 0:
            raise YouHaveReview
        
        return True
