from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.users.serializers import UserRetrieveSerializer


doc_user_me = swagger_auto_schema(
    responses={
        200: openapi.Response(description='', schema=UserRetrieveSerializer)
    }
)