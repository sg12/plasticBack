from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.service.serializers import *
from apps.common.schemas.tags import (
    doctor_tag,
    clinic_tag,
    profile_service_tag
)
from apps.common.schemas.description import doctor_or_clinic_alert


doc_doctor_service = extend_schema_view(
    get=extend_schema(
        summary='Список услуг',
        tags=doctor_tag,
        responses=ServiceSerializer(True)
    )
)

doc_clinic_service = extend_schema_view(
    get=extend_schema(
        summary='Список услуг',
        tags=clinic_tag,
        responses=ServiceSerializer(True)
    )
)

doc_profile_service = extend_schema_view(
    get=extend_schema(
        summary='Список услуг',
        description=doctor_or_clinic_alert,
        tags=profile_service_tag,
        responses=ServiceSerializer
    ),
    post=extend_schema(
        summary='Добавить услугу',
        description=doctor_or_clinic_alert,
        tags=profile_service_tag,
        request=ServiceCreateSerializer,
        responses=ServiceSerializer
    )
)

doc_profile_service_detail = extend_schema_view(
    delete=extend_schema(
        summary='Удалить услугу',
        description=doctor_or_clinic_alert,
        tags=profile_service_tag,
        responses=None
    ),
    patch=extend_schema(
        summary='Обновить данные услуги',
        description=doctor_or_clinic_alert,
        tags=profile_service_tag,
        request=ServiceUpdateSerializer,
        responses=ServiceSerializer
    )
)
