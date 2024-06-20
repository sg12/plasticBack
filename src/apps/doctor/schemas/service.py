from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from apps.service.serializers import ServiceSerializer
from apps.common.schemas.tags import doctor_tag


doc_doctor_service = extend_schema_view(
    get=extend_schema(
        tags=doctor_tag,
        summary='Список услуг',
        responses=ServiceSerializer(many=True),
    )
)
