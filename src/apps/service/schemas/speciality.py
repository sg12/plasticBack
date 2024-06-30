from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from apps.service.serializers import SpecialitySerializer
from pkg.schemas.tags import service_tag



doc_speciality = extend_schema_view(
    get=extend_schema(
        tags=service_tag,
        summary='Список специальностей',
        responses=SpecialitySerializer(many=True),
    )
)
