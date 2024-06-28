from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.user.serializers import AvatarSerializer
from pkg.schemas.tags import profile_tag


doc_avatar = extend_schema_view(
    patch=extend_schema(
        tags=profile_tag,
        summary='Обновить аватар',
        responses=AvatarSerializer,
    )
)
