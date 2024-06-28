from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.reception.serializers import *
from pkg.schemas.tags import profile_doctor_tag


doc_profile_reception_doctor = extend_schema_view(
    get=extend_schema(
        tags=profile_doctor_tag,
        summary='Список приемов',
        responses=ReceptionDoctorSerializer
    )
)

doc_profile_reception_doctor_detail = extend_schema_view(
    patch=extend_schema(
        tags=profile_doctor_tag,
        summary='Обновить данные приема',
        request=ReceptionDoctorUpdateSerializer,
        responses=ReceptionDoctorSerializer
    ),
    delete=extend_schema(
        tags=profile_doctor_tag,
        summary='Удалить запись на прием',
        responses=None,
    )
)
