from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.service.serializers import *
from pkg.schemas.tags import (
    doctor_tag,
    clinic_tag,
    profile_doctor_tag,
    profile_clinic_tag
)


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

doc_profile_doctor_service = extend_schema_view(
    get=extend_schema(
        summary='Список услуг',
        tags=profile_doctor_tag,
        responses=ServiceSerializer
    ),
    post=extend_schema(
        summary='Добавить услугу',
        tags=profile_doctor_tag,
        request=ServiceCreateSerializer,
        responses=ServiceSerializer
    )
)

doc_profile_doctor_service_detail = extend_schema_view(
    delete=extend_schema(
        summary='Удалить услугу',
        tags=profile_doctor_tag,
        responses=None
    ),
    patch=extend_schema(
        summary='Обновить данные услуги',
        tags=profile_doctor_tag,
        request=ServiceUpdateSerializer,
        responses=ServiceSerializer
    )
)

doc_profile_clinic_service = extend_schema_view(
    get=extend_schema(
        summary='Список услуг',
        description=profile_clinic_tag,
        tags=profile_clinic_tag,
        responses=ServiceSerializer
    )
)
