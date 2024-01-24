from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.clinics.serializers import *


doc_clinic_list = swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter(
            name='sort',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            enum=['rating', '-rating', 'reviews', '-reviews']
        ),
        openapi.Parameter(
            name='offset',
            default=0,
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_NUMBER,
        ),
        openapi.Parameter(
            name='limit',
            default=10,
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_NUMBER,
        ),
        openapi.Parameter(
            name='service',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            # enum=[el.slug for el in Service.objects.all()]
        ),
        openapi.Parameter(
            name='reception',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            enum=['clinic', 'private'],
        ),
        openapi.Parameter(
            name='price_min',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_NUMBER,
        ),
        openapi.Parameter(
            name='price_max',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_NUMBER,
        ),
        openapi.Parameter(
            name='metro',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
        ),
        openapi.Parameter(
            name='district',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
        ),
    ],
    responses={
        200: openapi.Response(description='', schema=ClinicListSerializer)
    }
)


doc_clinic_retrieve = swagger_auto_schema(
    responses={
        200: openapi.Response(description='', schema=ClinicRetrieveSerializer)
    }
)


doc_clinic_update = swagger_auto_schema(
    responses={
        200: openapi.Response(description='', schema=ClinicRetrieveSerializer)
    }
)
