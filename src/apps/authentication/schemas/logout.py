from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from pkg.schemas.tags import auth_tag


doc_logout = extend_schema_view(
    get=extend_schema(
        summary='Выход из аккаунта',
        tags=auth_tag,
        responses={204: None},
    )
)
