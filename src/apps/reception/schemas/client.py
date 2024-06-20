from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.reception.serializers import *
from apps.client.serializers import *
from apps.common.schemas.tags import profile_client_tag


doc_profile_reception_client = extend_schema_view(
    get=extend_schema(
        tags=profile_client_tag,
        summary='Список приемов',
        responses=ReceptionSerializer
    ),
    post=extend_schema(
        tags=profile_client_tag,
        summary='Добавить прием к врачу',
        request=ReceptionCreateSerializer,
        responses=ReceptionSerializer
    )
)

doc_profile_reception_client_detail = extend_schema_view(
    patch=extend_schema(
        tags=profile_client_tag,
        summary='Обновить данные о приеме',
        request=ReceptionUpdateSerializer,
        responses=ReceptionSerializer
    ),
    delete=extend_schema(
        tags=profile_client_tag,
        summary='Удалить запись на прием',
        responses=None,
    )
)
