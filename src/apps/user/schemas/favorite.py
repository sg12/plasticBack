from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.favorite.serializers import FavoriteCreateSerializer


doc_favorite = extend_schema_view(
    get=extend_schema(
        tags=['account favorite'],
        summary='Посмотреть список избранных врачей / клиник',
        responses=FavoriteCreateSerializer(many=True),
    )
)
