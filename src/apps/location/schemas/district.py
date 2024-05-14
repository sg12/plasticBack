from drf_spectacular.utils import extend_schema_view, extend_schema


doc_district = extend_schema_view(
    get=extend_schema(
        summary='Список районов',
        tags=['location'],
    )
)
