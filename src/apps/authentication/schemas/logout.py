from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from apps.authentication.serializers import (
    TokenSerializer,
    RegisterSerializer,
)

tags = ['auth']

doc_logout = extend_schema_view(
    get=extend_schema(
        tags=tags,
        responses={204: None},
    )
)
