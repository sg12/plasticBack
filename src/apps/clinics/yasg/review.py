from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'text': openapi.Schema(type=openapi.TYPE_STRING),
        'star': openapi.Schema(type=openapi.TYPE_NUMBER),
    },
    required=['text', 'star']
)

doc_review = swagger_auto_schema(
    request_body=request_body,
    responses={
        204: openapi.Response(description=''),
        404: openapi.Response(description='Не удалось добавить отзыв на данную клинику')
    }
)

doc_review_update = swagger_auto_schema(
    request_body=request_body,
    responses={
        204: openapi.Response(description=''),
        404: openapi.Response(description='', schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={'detail': 'Ошибка при редактировании отзыва'}
        ))
    }
)
