from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from apps.article.serializers import *
from apps.clinic.serializers import *
from apps.common.schemas.tags import clinic_tag, profile_clinic_tag


doc_clinic = extend_schema_view(
    get=extend_schema(
        summary='Список клиник',
        tags=clinic_tag,
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
        tags=clinic_tag,
        responses=ClinicRetrieveSerializer
    )
)

doc_profile_clinic_detail = extend_schema_view(
    get=extend_schema(
        summary='Данные клиники текущего профиля',
        tags=profile_clinic_tag,
        responses=ClinicRetrieveSerializer
    ),
    patch=extend_schema(
        summary='Обновляет поля клиники',
        tags=profile_clinic_tag,
        request=ClinicUpdateSerializer,
        responses=ClinicRetrieveSerializer
    )
)
