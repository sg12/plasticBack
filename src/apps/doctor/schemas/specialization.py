from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.doctor.serializers import *
from pkg.schemas.tags import service_tag


doc_dspecialization= extend_schema_view(
    get=extend_schema(
        summary='Список специализаций',
        tags=service_tag,
        responses=SpecializationSerializer(True)
    )
)
