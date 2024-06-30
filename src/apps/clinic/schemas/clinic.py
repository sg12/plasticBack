from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from apps.article.serializers import *
from apps.clinic.serializers import *
from pkg.schemas.tags import clinic_tag, profile_clinic_tag


doc_clinic = extend_schema_view(
    get=extend_schema(
        summary='Список клиник',
        tags=clinic_tag,
        parameters=[
            OpenApiParameter(
                name='search',
                type=str,
                location=OpenApiParameter.QUERY,
                description='Поиск по названию клиники'
            ),
            OpenApiParameter(
                name='ordering',
                type=str,
                location=OpenApiParameter.QUERY,
                description='''Сортировка по рейтингу `rating`, кол-ву отзывов `reviews`.
                Можно использовать их вместе `rating,reviews`'''
            ),
            OpenApiParameter(
                name='metro',
                type=str,
                location=OpenApiParameter.QUERY,
                description='Ближайщее метро (по slug)',
            ),
            OpenApiParameter(
                name='district',
                type=str,
                location=OpenApiParameter.QUERY,
                description='Регион (по slug)',
            ),
            OpenApiParameter(
                name='city',
                type=str,
                location=OpenApiParameter.QUERY,
                description='Город (по slug)',
            ),
            OpenApiParameter(
                name='price_min',
                type=int,
                location=OpenApiParameter.QUERY,
                description='Минимальная цена услиги',
            ),
            OpenApiParameter(
                name='price_max',
                type=int,
                location=OpenApiParameter.QUERY,
                description='Максимальная цена услуги',
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
