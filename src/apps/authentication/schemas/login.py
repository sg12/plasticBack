from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from apps.authentication.serializers import (
    TokenSerializer,
    LoginSerializer,
)
from pkg.schemas.tags import auth_tag


doc_login = extend_schema_view(
    post=extend_schema(
        summary='Авторизация',
        tags=auth_tag,
        request=LoginSerializer,
        responses=TokenSerializer,
    )
)
