from drf_spectacular.utils import extend_schema_view, extend_schema

doc_review = extend_schema_view(
    get=extend_schema(
        tags=['account review'],
        summary='Посмотреть отзывы на аккаунте'
    )
)