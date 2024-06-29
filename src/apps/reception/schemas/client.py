from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.reception.serializers import *
from apps.client.serializers import *
from pkg.schemas.tags import profile_client_tag


doc_profile_reception_client = extend_schema_view(
    get=extend_schema(
        tags=profile_client_tag,
        summary='Список приемов',
        responses=ReceptionClientSerializer
    ),
    post=extend_schema(
        tags=profile_client_tag,
        summary='Добавить прием к врачу',
        request=ReceptionClientCreateSerializer,
        responses=ReceptionClientSerializer
    )
)

doc_profile_reception_client_detail = extend_schema_view(
    patch=extend_schema(
        tags=profile_client_tag,
        summary='Обновить данные о приеме',
        request=ReceptionClientUpdateSerializer,
        responses=ReceptionClientSerializer
    ),
    delete=extend_schema(
        tags=profile_client_tag,
        summary='Удалить запись на прием',
        responses=None,
    )
)
