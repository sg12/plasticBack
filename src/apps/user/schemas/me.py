from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.user.serializers import UserUpdateSerializer
from apps.user.serializers import UserSerializer
from apps.common.schemas.tags import profile_tag


doc_me = extend_schema_view(
    get=extend_schema(
        tags=profile_tag,
        summary='Посмотреть данные своего профиля',
        responses=UserSerializer,
    ),
    patch=extend_schema(
        tags=profile_tag,
        summary='Обновляет данные пользователя',
        request=UserUpdateSerializer,
        responses=UserSerializer,
    )
)
