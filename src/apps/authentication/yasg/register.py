from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


doc_register = swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter('type', in_=openapi.IN_PATH, required=True, type=openapi.TYPE_STRING, enum=['client', 'surgeon', 'clinic']),
    ],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'password': openapi.Schema(type=openapi.TYPE_STRING),
            're_password': openapi.Schema(type=openapi.TYPE_STRING)
        },
        required=['email', 'password', 're_password']
    ),
)
