from rest_framework.permissions import exceptions
from rest_framework import status
from django.utils.translation import gettext_lazy as _


class IsDublicate(exceptions.APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Вы уже добавили этого пользователя в список избранных')
    default_code = 'bad_request'
