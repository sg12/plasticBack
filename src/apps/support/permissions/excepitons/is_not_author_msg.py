from rest_framework.permissions import exceptions
from rest_framework import status
from django.utils.translation import gettext_lazy as _


class IsNotAuthorMsg(exceptions.APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _('Вы не являетесь автором сообщения')
    default_code = 'permission_denied'
