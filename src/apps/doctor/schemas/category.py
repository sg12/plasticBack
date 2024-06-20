from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from apps.doctor.serializers import CategorySerializer
from .tags import doctor_tag


doc_category = extend_schema_view(
    get=extend_schema(
        tags=doctor_tag,
        summary='Список категорий',
        responses=CategorySerializer(many=True),
    )
)
