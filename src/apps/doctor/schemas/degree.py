from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from apps.doctor.serializers import DegreeSerializer
from .tags import doctor_tag


doc_degree = extend_schema_view(
    get=extend_schema(
        tags=doctor_tag,
        summary='Список ученных степеней',
        responses=DegreeSerializer(many=True),
    )
)
