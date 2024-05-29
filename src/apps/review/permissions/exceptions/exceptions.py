from rest_framework.permissions import exceptions
from rest_framework import status
from django.utils.translation import gettext_lazy as _


class UserDoesNotExist(exceptions.APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Нет такого пользователя')
    default_code = 'bad_request'


class IsNotAuthorProfile(exceptions.APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _('Вы не можете отвечать на отзыв стороннего профиля')
    default_code = 'permission_denied'


class IsNotAuthorReply(exceptions.APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _('Вы не являетесь автором комментария')
    default_code = 'permission_denied'
