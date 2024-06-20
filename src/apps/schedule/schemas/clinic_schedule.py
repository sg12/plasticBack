from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.schedule.serializers import (
    ClinicScheduleSerializer,
    ClinicScheduleCreateSerializer,
    ClinicScheduleUpdateSerializer
)
from apps.common.schemas.tags import clinic_tag


doc_clinic_schedule = extend_schema_view(
    get=extend_schema(
        tags=clinic_tag,
        summary='Рабочее расписание',
        responses=ClinicScheduleSerializer(many=True)
    )
)

doc_profile_clinic_schedule = extend_schema_view(
    get=extend_schema(
        tags=clinic_tag,
        summary='Рабочее расписание',
        responses=ClinicScheduleSerializer(many=True)
    ),
    post=extend_schema(
        tags=clinic_tag,
        summary='Добавить рассписание',
        request=ClinicScheduleCreateSerializer,
        responses=ClinicScheduleSerializer
    )
)

doc_profile_clinic_schedule_detail = extend_schema_view(
    patch=extend_schema(
        tags=clinic_tag,
        summary='Обновить рассписание',
        request=ClinicScheduleUpdateSerializer,
        responses=ClinicScheduleSerializer
    ),
    delete=extend_schema(
        tags=clinic_tag,
        summary='Добавить рассписание',
        request=ClinicScheduleCreateSerializer,
        responses=ClinicScheduleSerializer
    )
)
