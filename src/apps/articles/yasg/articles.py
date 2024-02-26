from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.articles.serializers import ArticleReadSerializer


doc_articles_list = swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter(
            name='limit',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_NUMBER,
            default=10,
        ),
        openapi.Parameter(
            name='offset',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_NUMBER,
            default=0,
        ),
        openapi.Parameter(
            name='search',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING
        ),
        openapi.Parameter(
            name='sort',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            enum=['id']
        ),
    ],
    responses={
        200: openapi.Response(description='', schema=ArticleReadSerializer)
    }
)