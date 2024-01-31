from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.clinics.serializers import ClinicListSerializer
from apps.services.serializers import (
    ServiceRetrieveSerializer,
    ServiceCreateSerializer,
    ServiceUpdateSerializer,
)


doc_service_create = swagger_auto_schema(
    request_body=ServiceCreateSerializer,
    responses={
        200: openapi.Response('', ServiceRetrieveSerializer),
    }
)

doc_service_update = swagger_auto_schema(
    request_body=ServiceUpdateSerializer,
    responses={
        200: openapi.Response('', ServiceRetrieveSerializer),
    }
)

doc_service_slug_get = swagger_auto_schema(
    responses={
        200: openapi.Response('', ClinicListSerializer(many=True)),
    }
)
