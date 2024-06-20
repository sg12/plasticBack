from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.reception.serializers import *
from apps.common.schemas.tags import profile_doctor_tag


doc_profile_reception_doctor = extend_schema_view(
    get=extend_schema(
        tags=profile_doctor_tag,
        summary='Список приемов',
        responses=ReceptionSerializer
    )
)

doc_profile_reception_doctor_detail = extend_schema_view(
    delete=extend_schema(
        tags=profile_doctor_tag,
        summary='Удалить запись на прием',
        responses=None,
    )
)
