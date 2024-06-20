from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.reception.serializers import *
from apps.client.serializers import *
from apps.common.schemas.tags import profile_clinic_tag


doc_profile_reception_clinic = extend_schema_view(
    get=extend_schema(
        tags=profile_clinic_tag,
        summary='Список приемов',
        responses=ReceptionSerializer
    )
)

doc_profile_reception_clinic_detail = extend_schema_view(
    patch=extend_schema(
        tags=profile_clinic_tag,
        summary='Обновить данные о приеме',
        request=ReceptionUpdateSerializer,
        responses=ReceptionSerializer
    ),
    delete=extend_schema(
        tags=profile_clinic_tag,
        summary='Удалить запись на прием',
        responses=None,
    )
)
