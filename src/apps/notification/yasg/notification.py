from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.clinics.serializers import *
from apps.services.models import ServiceInfo
from apps.clinics.models import Metro, District
from django.db.utils import OperationalError
from apps.notification.serializers import NotificationSerializer

doc_notification_list = swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter(
            name='test',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
        ),
    ],
    responses={
        200: openapi.Response(description='', schema=NotificationSerializer)
    }
)

doc_notification_create = swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter(
            name='test',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
        ),
    ],
    responses={
        200: openapi.Response(description='', schema=NotificationSerializer)
    }
)