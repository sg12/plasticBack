from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from apps.doctor.serializers import SpecialitySerializer
from .tags import doctor_tag


doc_speciality = extend_schema_view(
    get=extend_schema(
        tags=doctor_tag,
        summary='Список специальностей',
        responses=SpecialitySerializer(many=True),
    )
)
