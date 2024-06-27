from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.user.serializers import UserSerializer
from pkg.schemas.tags import profile_tag


doc_user = extend_schema_view(
    get=extend_schema(
        tags=profile_tag,
        summary='Посмотреть данные',
        responses=UserSerializer,
    )
)
