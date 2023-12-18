from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.surgeons.serializers import SurgeonListSerializer, SurgeonRetrieveSerializer


doc_surgeon_list = swagger_auto_schema(
    responses={
        200: openapi.Response('', SurgeonListSerializer(many=True)),
    }
)

doc_surgeon_retrieve_update = swagger_auto_schema(
    responses={
        200: openapi.Response('', SurgeonRetrieveSerializer),
    }
)