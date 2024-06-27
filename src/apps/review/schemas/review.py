from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.review.serializers import *
from apps.clinic.serializers import *
from pkg.schemas.tags import *


doc_review_doctor = extend_schema_view(
    get=extend_schema(
        tags=doctor_tag,
        summary='Список отзывов',
        responses=ReviewSerializer(many=True)
    ),
    post=extend_schema(
        tags=doctor_tag,
        summary='Добавить отзыв',
        request=ReviewCreateSerializer,
        responses=ReviewSerializer(many=True)
    ),
    patch=extend_schema(
        tags=doctor_tag,
        summary='Обновить данные отзыва',
        request=ReviewUpdateSerializer,
        responses=ReviewSerializer
    ),
    delete=extend_schema(
        tags=doctor_tag,
        summary='Удалить отзыв',
        responses=None
    )
)

doc_review_clinic = extend_schema_view(
    get=extend_schema(
        tags=clinic_tag,
        summary='Список отзывов',
        responses=ReviewSerializer(many=True)
    ),
    post=extend_schema(
        tags=clinic_tag,
        summary='Добавить отзыв',
        request=ReviewCreateSerializer,
        responses=ReviewSerializer(many=True)
    ),
    patch=extend_schema(
        tags=clinic_tag,
        summary='Обновить данные отзыва',
        request=ReviewUpdateSerializer,
        responses=ReviewSerializer
    ),
    delete=extend_schema(
        tags=clinic_tag,
        summary='Удалить отзыв',
        responses=None
    )
)

doc_profile_review = extend_schema_view(
    delete=extend_schema(
        tags=profile_tag,
        summary='Список отзывов на профиле',
        responses=ReviewSerializer(many=True)
    )
)
