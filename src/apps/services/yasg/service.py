from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.clinics.serializers import ClinicListSerializer


doc_service_slug_get = swagger_auto_schema(
    responses={
        200: openapi.Response('', ClinicListSerializer(many=True)),
    }
)
