from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.article.serializers import *
from apps.clinic.serializers import *


doc_license = extend_schema_view(
    get=extend_schema(
        summary='Список лицензий конкретного пользователя',
        tags=['user'],
    )
)

doc_profile_license = extend_schema_view(
    get=extend_schema(
        summary='Список лицензий текущего профиля',
        tags=['profile'],
    ),
    post=extend_schema(
        summary='Добавить новую лицензию',
        tags=['profile'],
    )
)

doc_profile_license_detail = extend_schema_view(
    delete=extend_schema(
        summary='Удалить конкретную лицензию',
        tags=['profile'],
    )
)
