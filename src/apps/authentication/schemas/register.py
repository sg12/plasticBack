from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from apps.authentication.serializers import (
    TokenSerializer,
    RegisterSerializer,
)

tags = ['auth']

doc_register = extend_schema_view(
    post=extend_schema(
        tags=tags,
        request=RegisterSerializer,
        responses={201: TokenSerializer},
    )
)
