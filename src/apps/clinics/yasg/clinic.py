from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.clinics.serializers import *
from apps.services.models import ServiceInfo
from apps.clinics.models import Metro, District
from django.db.utils import OperationalError


doc_clinic_list = swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter(
            name='limit',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_NUMBER,
        ),
        openapi.Parameter(
            name='page',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_NUMBER,
        ),
        openapi.Parameter(
            name='search',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING
        ),
        openapi.Parameter(
            name='service',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            enum=[el.slug for el in ServiceInfo.objects.all()],
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
            enum=[el.slug for el in Metro.objects.all()],
        ),
        openapi.Parameter(
            name='district',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            enum=[el.slug for el in District.objects.all()]
        ),
        openapi.Parameter(
            name='sort',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            enum=['rating', 'reviews']
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
