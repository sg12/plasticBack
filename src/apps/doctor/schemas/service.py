from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from apps.service.serializers import ServiceSerializer

tags = ['doctor service']

doc_doctor_service = extend_schema_view(
    get=extend_schema(
        tags=tags,
        responses=ServiceSerializer(many=True),
    )
)
