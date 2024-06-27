from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.support.serializers import *
from pkg.schemas.tags import support_tag


doc_message = extend_schema_view(
    get=extend_schema(
        summary='Список сообщений',
        tags=support_tag,
        responses=TicketCreateSerializer(True)
    ),
    post=extend_schema(
        summary='Создать сообщение',
        tags=support_tag,
        request=TicketCreateSerializer,
        responses=TicketCreateSerializer
    )
)

doc_message_detail = extend_schema_view(
    patch=extend_schema(
        summary='Обновить данные сообщения',
        tags=support_tag,
        request=TicketUpdateSerializer,
        responses=TicketCreateSerializer
    ),
    delete=extend_schema(
        summary='Удалить сообщение',
        tags=support_tag,
        responses=None
    )
)
