from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.doctor.serializers import (
    DoctorSerializer,
    DoctorUpdateSerializer,
)


tags = ['user doctor']

doc_doctor = extend_schema_view(
    get=extend_schema(
        tags=tags,
        summary='Посмотреть данные доктора',
        responses=DoctorSerializer,
    ),
    patch=extend_schema(
        tags=tags,
        summary='Обновляет данные доктора',
        request=DoctorUpdateSerializer,
        responses=DoctorSerializer,
    )
)
