from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.user.serializers import UserUpdateSerializer
from apps.user.serializers import UserSerializer


tags = ['me']

doc_me = extend_schema_view(
    get=extend_schema(
        tags=tags,
        summary='Посмотреть данные аккаунта',
        description='Ответ может быть разным в зависимости от пользователя',
        responses=UserSerializer,
    ),
    patch=extend_schema(
        tags=tags,
        summary='Обновляет данные пользователя',
        request=UserUpdateSerializer,
        responses=UserSerializer,
    )
)
