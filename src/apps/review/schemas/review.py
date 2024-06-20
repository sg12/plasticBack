from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.review.serializers import *
from apps.clinic.serializers import *
from apps.common.schemas.tags import (
    profile_tag, 
    review_tag,
    doctor_tag,
    clinic_tag
)


doc_review_doctor = extend_schema_view(
    get=extend_schema(
        tags=review_tag+doctor_tag,
        summary='Список отзывов доктора',
        responses=ReviewSerializer(many=True)
    ),
    post=extend_schema(
        tags=review_tag+doctor_tag,
        summary='Добавить отзыв для доктора',
        request=ReviewCreateSerializer,
        responses=ReviewSerializer(many=True)
    )
)

doc_review_clinic = extend_schema_view(
    get=extend_schema(
        tags=review_tag+clinic_tag,
        summary='Список отзывов клиники',
        responses=ReviewSerializer(many=True)
    ),
    post=extend_schema(
        tags=review_tag+clinic_tag,
        summary='Добавить отзыв для клиники',
        request=ReviewCreateSerializer,
        responses=ReviewSerializer(many=True)
    )
)

doc_review_detail = extend_schema_view(
    patch=extend_schema(
        tags=review_tag,
        summary='Обновить данные отзыва',
        request=ReviewUpdateSerializer,
        responses=ReviewSerializer
    ),
    delete=extend_schema(
        tags=review_tag,
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
