from rest_framework import permissions
from apps.favorite.models import Favorite
from apps.review.models import *
from .exceptions import *


class DontDublicate(permissions.BasePermission):
    '''
    Выдаст ошибку если аккаунт уже есть в списке избранных.
    Рабочий метод: `POST`.
    '''
    
    def has_permission(self, request, view):
        if request.method != 'POST':
            return True
        
        user_id = request.data.get('user')
        
        favorite = Favorite.objects.filter(
            author=request.user,
            user_id=user_id,
        ).first()
        
        if favorite:
            raise IsDublicate
        
        return True
