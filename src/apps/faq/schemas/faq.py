from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from apps.faq.serializers import *
from .tags import faq_tag


doc_faq = extend_schema_view(
    get=extend_schema(
        tags=faq_tag,
        summary='Список часто задаваемых вопросов',
        responses=FAQSerializer
    )
)
