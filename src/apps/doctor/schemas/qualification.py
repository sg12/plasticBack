from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from apps.doctor.serializers import QualificationSerializer
from .tags import doctor_tag
from apps.common.schemas.tags import profile_doctor_tag
from apps.common.schemas.description import doctor_alert


doc_qualification = extend_schema_view(
    get=extend_schema(
        tags=doctor_tag,
        summary='Список квалификаций',
        responses=QualificationSerializer(many=True),
    )
)

doc_profile_qualification = extend_schema_view(
    get=extend_schema(
        tags=profile_doctor_tag,
        summary='Список квалификаций',
        description=doctor_alert,
        responses=QualificationSerializer,
    ),
    post=extend_schema(
        tags=profile_doctor_tag,
        summary='Добавить новую квалификацию',
        description=doctor_alert,
        responses={201: QualificationSerializer},
    )
)

doc_profile_qualification_detail = extend_schema_view(
    patch=extend_schema(
        tags=profile_doctor_tag,
        summary='Обновить данные об квалификации',
        description=doctor_alert,
        responses=QualificationSerializer,
    ),
    delete=extend_schema(
        tags=profile_doctor_tag,
        description=doctor_alert,
        summary='Удалить данные об квалицикации',
    )
)
