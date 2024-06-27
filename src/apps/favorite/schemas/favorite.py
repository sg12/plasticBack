from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.favorite.serializers import *
from pkg.schemas.tags import favorite_tag
from pkg.schemas.description import client_alert


doc_favorite_doctor = extend_schema_view(
    get=extend_schema(
        tags=favorite_tag,
        summary='Посмотреть список избранных врачей',
        description=client_alert,
        responses=FavoriteDoctorSerializer(many=True),
    )
)

doc_favorite_clinic = extend_schema_view(
    get=extend_schema(
        tags=favorite_tag,
        summary='Посмотреть список избранные клиники',
        description=client_alert,
        responses=FavoriteClinicSerializer(many=True),
    )
)

doc_add_favorite = extend_schema_view(
    post=extend_schema(
        tags=favorite_tag,
        summary='Добавить в избранные',
        description=client_alert,
        responses=None,
    )
)

doc_favorite_detail = extend_schema_view(
    delete=extend_schema(
        tags=favorite_tag,
        summary='Удалить из избранных',
        description=client_alert
    )
)
