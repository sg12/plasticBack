from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.favorite.serializers import *
from pkg.schemas.tags import profile_client_tag
from pkg.schemas.description import client_alert


doc_favorite_doctor = extend_schema_view(
    get=extend_schema(
        tags=profile_client_tag,
        summary='Посмотреть список избранных врачей',
        responses=FavoriteDoctorSerializer(many=True),
    )
)

doc_favorite_clinic = extend_schema_view(
    get=extend_schema(
        tags=profile_client_tag,
        summary='Посмотреть список избранных клиник',
        responses=FavoriteClinicSerializer(many=True),
    )
)

doc_add_favorite = extend_schema_view(
    post=extend_schema(
        tags=profile_client_tag,
        summary='Добавить в избранные',
        responses=None,
    )
)

doc_favorite_detail = extend_schema_view(
    delete=extend_schema(
        tags=profile_client_tag,
        summary='Удалить из избранных'
    )
)
