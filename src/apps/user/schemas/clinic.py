from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from apps.clinic.serializers import (
    ClinicSerializer,
    ClinicUpdateSerializer,
)


tags = ['user clinic']

doc_clinic = extend_schema_view(
    get=extend_schema(
        tags=tags,
        summary='Посмотреть данные клиники',
        responses=ClinicSerializer,
    ),
    patch=extend_schema(
        tags=tags,
        summary='Обновляет данные клиники',
        request=ClinicUpdateSerializer,
        responses=ClinicSerializer,
    )
)
