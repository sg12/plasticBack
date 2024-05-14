from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from apps.authentication.serializers import (
    TokenSerializer,
    LoginSerializer,
)

tags = ['auth']

doc_login = extend_schema_view(
    post=extend_schema(
        tags=tags,
        request=LoginSerializer,
        responses=TokenSerializer,
    )
)
