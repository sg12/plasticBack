from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.review.serializers import *
from apps.clinic.serializers import *
from pkg.schemas.tags import review_tag
from pkg.schemas.description import doctor_or_clinic_alert


doc_reply = extend_schema_view(
    get=extend_schema(
        tags=review_tag,
        summary='Список ответов на отзыв',
        responses=ReplySerializer(many=True)
    ),
    post=extend_schema(
        tags=review_tag,
        summary='Добавить отзыв для доктора',
        description=doctor_or_clinic_alert,
        request=ReplyCreateSerializer,
        responses=ReplySerializer(many=True)
    )
)

doc_reply_detail = extend_schema_view(
    patch=extend_schema(
        tags=review_tag,
        summary='Обновить данные ответа',
        request=ReplyUpdateSerializer,
        responses=ReplySerializer
    ),
    delete=extend_schema(
        tags=review_tag,
        summary='Удалить ответ',
        responses=None
    )
)
