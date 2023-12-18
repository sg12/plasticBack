from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.services.models import Service
from apps.surgeons.models import Specialtie
from apps.clinics.serializers import *


doc_clinic_list = swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter(
            name='service',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            enum=[el.slug for el in Service.objects.all()]
        ),
        openapi.Parameter(
            name='spec',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            enum=[el.slug for el in Specialtie.objects.all()]
        ),
        openapi.Parameter(
            name='sort',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            enum=['rating', '-rating']
        ),
    ],
    responses={
        200: openapi.Response(description='', schema=ClinicListSerializer)
    }
)


doc_clinic_retrieve = swagger_auto_schema(
    responses={
        200: openapi.Response(description='', schema=ClinicReadSerializer)
    }
)


doc_clinic_update = swagger_auto_schema(
    responses={
        200: openapi.Response(description='', schema=ClinicReadSerializer)
    }
)
