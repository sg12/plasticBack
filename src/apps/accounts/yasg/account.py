from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import AccountUpdateSerializer


doc_account_retrieve = swagger_auto_schema(
    responses={
        200: openapi.Response('Ответ генерируется в зависимости от пользователя')
    },
)


doc_account_update = swagger_auto_schema(
    request_body=AccountUpdateSerializer()
)