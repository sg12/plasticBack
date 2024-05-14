from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.clinic.serializers import ClinicListSerializer
from apps.service.serializers import (
    ServiceSerializer,
    ServiceCreateSerializer,
    ServiceUpdateSerializer,
)

__BASETAG__ = ("account services", )

doc_service_create = swagger_auto_schema(
    tags=__BASETAG__,
    request_body=ServiceCreateSerializer,
    responses={
        200: openapi.Response('', ServiceSerializer),
    }
)

doc_service_update = swagger_auto_schema(
    tags=__BASETAG__,
    request_body=ServiceUpdateSerializer,
    responses={
        200: openapi.Response('', ServiceSerializer),
    }
)

doc_service_slug_get = swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter('type', in_=openapi.IN_QUERY, required=True, type=openapi.TYPE_STRING, enum=['doctor', 'clinic']),
    ],
    responses={
        200: openapi.Response('', ClinicListSerializer(many=True)),
    }
)
