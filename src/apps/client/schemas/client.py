from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.reception.serializers import *
from apps.client.serializers import *
from pkg.schemas.tags import client_tag, profile_client_tag


doc_client = extend_schema_view(
    get=extend_schema(
        tags=client_tag,
        summary='Данные клиента',
        responses=ClientSerializer
    )
)

doc_profile_client = extend_schema_view(
    get=extend_schema(
        tags=profile_client_tag,
        summary='Данные клиента текущего профиля',
        responses=ClientSerializer
    ),
    patch=extend_schema(
        tags=profile_client_tag,
        summary='Обновить данные клиента',
        request=ClientUpdateSerializer,
        responses=ClientSerializer
    )
)
