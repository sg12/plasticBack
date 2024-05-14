from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.service.serializers import (
    ServiceSerializer,
    ServiceCreateSerializer,
    ServiceUpdateSerializer,
)


tags = ['account service']

doc_service = extend_schema_view(
    get=extend_schema(
        tags=tags,
        summary='Посмотреть услуги',
        responses=ServiceSerializer,
    ),
    post=extend_schema(
        tags=tags,
        summary='Добавить услугу',
        request=ServiceCreateSerializer,
        responses={201: ServiceSerializer},
    )
)

doc_service_detail = extend_schema_view(
    patch=extend_schema(
        tags=tags,
        summary='Обновить данные услуги',
        request=ServiceUpdateSerializer,
        responses=ServiceSerializer,
    ),
    delete=extend_schema(
        tags=tags,
        summary='Удалить услугу'
    )
)
