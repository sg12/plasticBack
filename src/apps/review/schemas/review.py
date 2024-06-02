from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from apps.review.serializers import *


tags=['review']

doc_review = extend_schema_view(
    get=extend_schema( 
        summary='Список обзоров',
        tags=tags,
    ),
    post=extend_schema(
        summary='Добавление обзоров',
        tags=tags,
    )
)

doc_detail_review = extend_schema_view(
    get=extend_schema(
        summary='Данные конкретного обзора',
        tags=tags,
    ),
    post=extend_schema(
        summary='Добавление конкретного обзора',
        tags=tags,
    )
)