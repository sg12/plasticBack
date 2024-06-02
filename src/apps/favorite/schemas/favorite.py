from drf_spectacular.utils import(
    extend_schema_view,
    extend_schema,
)

tags=['favorite']

doc_delete_favorite = extend_schema_view(
    delete=extend_schema(
        summary='Удаление избранного',
        tags=tags,
    )
)