from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.clinic.serializers import ClinicListSerializer
from apps.service.serializers import (
    ServiceSerializer,
    ServiceCreateSerializer,
    ServiceUpdateSerializer,
)


class ServiceSwagger:
    list_schemas = {}

    def add(self, action: str, auto_schema):
        self.list_schemas[action] = auto_schema

    def
