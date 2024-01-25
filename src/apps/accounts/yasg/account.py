from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


doc_account = swagger_auto_schema(
    responses={
        200: openapi.Response('Ответ генерируется в зависимости от пользователя')
    },
)