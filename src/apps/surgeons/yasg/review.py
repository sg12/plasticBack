from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'text': openapi.Schema(type=openapi.TYPE_STRING),
        'rating': openapi.Schema(type=openapi.TYPE_NUMBER),
    },
    required=['text', 'rating']
)

doc_review_create = swagger_auto_schema(
    request_body=request_body,
    responses={
        204: openapi.Response(description=''),
        404: openapi.Response(description='Не удалось добавить отзыв на данный аккаунт')
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
