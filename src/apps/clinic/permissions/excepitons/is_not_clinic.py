from rest_framework.permissions import exceptions
from rest_framework import status
from django.utils.translation import gettext_lazy as _


class IsNotClinic(exceptions.APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _('Вы не являетесь клиникой')
    default_code = 'bad_request'
