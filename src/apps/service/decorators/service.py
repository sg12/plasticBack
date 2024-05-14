from functools import wraps
from apps.user.models import Role
from django.http.response import Http404


def service_access(func):
    """
    Проверяет можно ли обращаться к услугам пользователя.
    Если нет, то вернет статус 404.
    """

    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role.name not in (Role.DOCTOR, Role.CLINIC):
                return Http404
        return func(request, *args, **kwargs)
    return wrapper
