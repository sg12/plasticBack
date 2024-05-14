from drf_spectacular.utils import extend_schema_view, extend_schema


doc_metro = extend_schema_view(
    get=extend_schema(
        summary='Список метро',
        tags=['location'],
    )
)
