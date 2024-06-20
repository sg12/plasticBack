from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from apps.article.serializers import *


tags = ['article']

doc_article_list = extend_schema_view(
    get=extend_schema(
        tags=tags,
        summary='Список статей',
        responses=ArticleSerializer(many=True),
        parameters=[
            OpenApiParameter(
                name='page',
                type=str,
                location=OpenApiParameter.QUERY,
                description='Номер страницы'
            ),
            OpenApiParameter(
                name='limit',
                type=int,
                location=OpenApiParameter.QUERY,
                description='Количество результатов, возвращаемых на страницу'
            ),
            OpenApiParameter(
                name='search',
                type=str,
                location=OpenApiParameter.QUERY,
                description='Поиск по названию статьи и имени ее автора'
            )
        ]
    )
)

doc_article_retrieve = extend_schema_view(
    get=extend_schema(
        summary='Данные статьи',
        tags=tags,
        responses=ArticleSerializer,
    )
)
