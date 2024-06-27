from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from apps.doctor.serializers import WorkplaceSerializer
from .tags import doctor_tag
from pkg.schemas.tags import profile_doctor_tag
from pkg.schemas.description import doctor_alert


doc_workplace = extend_schema_view(
    get=extend_schema(
        tags=doctor_tag,
        summary='Список рабочих мест',
        responses=WorkplaceSerializer(many=True),
    )
)

doc_profile_workplace = extend_schema_view(
    get=extend_schema(
        tags=profile_doctor_tag,
        summary='Список рабочих мест',
        description=doctor_alert,
        responses=WorkplaceSerializer,
    ),
    post=extend_schema(
        tags=profile_doctor_tag,
        summary='Добавить рабочее место',
        description=doctor_alert,
        responses={201: WorkplaceSerializer},
    )
)

doc_profile_workplace_detail = extend_schema_view(
    patch=extend_schema(
        tags=profile_doctor_tag,
        summary='Обновить данные об рабочем месте',
        description=doctor_alert,
        responses=WorkplaceSerializer,
    ),
    delete=extend_schema(
        tags=profile_doctor_tag,
        description=doctor_alert,
        summary='Удалить данные об рабочем месте',
    )
)
