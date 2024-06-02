from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)

from apps.faq.serializers import FAQListSerializer

tags=['faq']

doc_faq = extend_schema_view(
    get=extend_schema(
        summary='Список FAQ',
        tags=tags,
        responses=FAQListSerializer(many=True),
    )
)