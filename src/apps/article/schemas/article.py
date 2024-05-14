from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from apps.article.serializers import *


tags = ['article']

doc_article_list = extend_schema_view(
    get=extend_schema(
        tags=tags,
        responses={200: ArticleSerializer(many=True)},
        parameters=[
            OpenApiParameter(
                name='limit',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description='Количество результатов, возвращаемых на страницу'
            ),
            OpenApiParameter(
                name='ordering',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Сортировка',
                enum=['created_at']
            ),
            OpenApiParameter(
                name='page',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
                description='Номер страницы в разбитом на страницы результирующем наборе'
            ),
            OpenApiParameter(
                name='search',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Поиск по названию статьи и имени ее автора'
            ),
        ],
    )
)


doc_article_retrieve = extend_schema_view(
    get=extend_schema(
        tags=tags,
        responses=ArticleSerializer,
    )
)
