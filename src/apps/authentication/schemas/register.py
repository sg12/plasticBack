from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter
)
from apps.authentication.serializers import (
    TokenSerializer,
    RegisterSerializer,
)
from pkg.schemas.tags import auth_tag
from pkg.serializers import ErrorSerializer


doc_register = extend_schema_view(
    post=extend_schema(
        summary='Регистрация',
        tags=auth_tag,
        request=RegisterSerializer,
        responses={201: TokenSerializer},
        parameters=[
            OpenApiParameter(
                name='role',
                type=str,
                location=OpenApiParameter.PATH,
                description='Используйте `client`, `doctor` или `clinic`'
            )
        ]
    )
)
