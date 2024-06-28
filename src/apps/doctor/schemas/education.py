from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from apps.doctor.serializers import EducationSerializer
from .tags import doctor_tag
from pkg.schemas.tags import profile_doctor_tag
from pkg.schemas.description import doctor_alert



doc_education = extend_schema_view(
    get=extend_schema(
        tags=doctor_tag,
        summary='Список образований',
        responses=EducationSerializer(many=True),
    )
)

doc_profile_education = extend_schema_view(
    get=extend_schema(
        tags=profile_doctor_tag,
        summary='Список образований',
        description=doctor_alert,
        responses=EducationSerializer,
    ),
    post=extend_schema(
        tags=profile_doctor_tag,
        summary='Добавить новое образование',
        description=doctor_alert,
        responses={201: EducationSerializer},
    )
)

doc_profile_education_detail = extend_schema_view(
    patch=extend_schema(
        tags=profile_doctor_tag,
        summary='Обновить данные об образовании',
        responses=EducationSerializer,
    ),
    delete=extend_schema(
        tags=profile_doctor_tag,
        summary='Удалить данные об образовании',
    )
)
