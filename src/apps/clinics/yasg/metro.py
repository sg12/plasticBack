from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.clinics.serializers import MetroListSerializer


doc_metro_list = swagger_auto_schema(
    responses={
        200: openapi.Response(description='', schema=MetroListSerializer(many=True))
    }
)