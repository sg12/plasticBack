from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.clinics.serializers import DistrictListSerializer


doc_district_list = swagger_auto_schema(
    responses={
        200: openapi.Response(description='', schema=DistrictListSerializer(many=True))
    }
)