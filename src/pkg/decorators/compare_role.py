from functools import wraps
from apps.user.models import User
from django.shortcuts import get_object_or_404
from django.http.response import Http404


def compare_role(role_name: str):
    """
    Сравнивает роль искомого пользователя и `role_name`, 
    в случае несоответвия вызовет Http404.
    
    Для корректной работы декоратора, в `url` должна быть переменная `pk`.
    """
    
    def wrap(func): 
        @wraps(func)
        def inner_wrap(*args, **kwargs):
            user = get_object_or_404(User, pk=kwargs.get('pk'))
            if user.role != role_name:
                raise Http404
            return func(*args, *kwargs)
        return inner_wrap
    return wrap