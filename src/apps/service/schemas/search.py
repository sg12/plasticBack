from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from apps.service.serializers import *
from pkg.schemas.tags import service_tag


doc_search_doctor_service = extend_schema_view(
    get=extend_schema(
        summary='Поиск докторов по услуге',
        tags=service_tag,
        parameters=[
            OpenApiParameter(
                name='id',
                type=int,
                location=OpenApiParameter.PATH,
                description='ID специальности'
            )
        ],
        responses=DoctorServiceSerializer(True)
    )
)

doc_search_clinic_service = extend_schema_view(
    get=extend_schema(
        summary='Поиск клиник по услуге',
        tags=service_tag,
        parameters=[
            OpenApiParameter(
                name='id',
                type=int,
                location=OpenApiParameter.PATH,
                description='ID специальности'
            )
        ],
        responses=ClinicServiceSerializer(True)
    )
)
