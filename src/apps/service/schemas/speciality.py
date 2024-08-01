from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from apps.service.serializers import SpecialtySerializer
from pkg.schemas.tags import service_tag



doc_speciality = extend_schema_view(
    get=extend_schema(
        tags=service_tag,
        summary='Список специальностей',
        responses=SpecialtySerializer(many=True),
        description='Специальность - вид услуг, которые доктор может предоставить пользователям'
    )
)
