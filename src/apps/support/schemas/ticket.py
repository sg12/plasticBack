from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.support.serializers import *
from pkg.schemas.tags import support_tag


doc_ticket = extend_schema_view(
    get=extend_schema(
        summary='Список тикетов',
        tags=support_tag,
        responses=TicketSerializer(True)
    ),
    post=extend_schema(
        summary='Создать тикет',
        tags=support_tag,
        request=TicketCreateSerializer,
        responses=TicketSerializer
    )
)

doc_ticket_detail = extend_schema_view(
    patch=extend_schema(
        summary='Обновить данные тикета',
        tags=support_tag,
        request=TicketUpdateSerializer,
        responses=TicketSerializer
    ),
    delete=extend_schema(
        summary='Удалить тикет',
        tags=support_tag,
        responses=None
    )
)
