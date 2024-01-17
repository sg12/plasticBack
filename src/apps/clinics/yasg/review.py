from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


doc_review = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'text': openapi.Schema(type=openapi.TYPE_STRING),
            'star': openapi.Schema(type=openapi.TYPE_NUMBER),
        },
        required=['text', 'star']
    ),
    responses={
        201: openapi.Response(description='')
    }
)