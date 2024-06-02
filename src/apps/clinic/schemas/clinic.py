from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from apps.article.serializers import *
from apps.clinic.serializers import *


doc_clinic = extend_schema_view(
    get=extend_schema(
        summary='Список клиник',
        tags=['clinic'],
        parameters=[
            OpenApiParameter(
                name='search',
                type=str,
                location=OpenApiParameter.QUERY,
                description='Поиск по названию статьи и имени ее автора'
            ),
            OpenApiParameter(
                name='ordering',
                type=str,
                location=OpenApiParameter.QUERY,
                description='Сортировка по рейтингу и кол-ву отзывов',
                enum=['rating', 'reviews_count']
            ),
        ]
    )
)

doc_clinic_detail = extend_schema_view(
    get=extend_schema(
        summary='Данные конкретной клиники',
        tags=['clinic'],
        responses=ClinicRetrieveSerializer
    )
)

doc_profile_clinic_detail = extend_schema_view(
    get=extend_schema(
        summary='Данные клиники текущего профиля',
        tags=['profile'],
        responses=ClinicRetrieveSerializer
    ),
    patch=extend_schema(
        summary='Обновляет поля клиники',
        tags=['profile'],
        request=ClinicUpdateSerializer,
        responses=ClinicRetrieveSerializer
    ),
    put=extend_schema(
        summary='Обновляет клинику',
        tags=['profile'],
    )
        
)
