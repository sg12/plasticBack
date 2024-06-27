from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiParameter
)
from apps.doctor.serializers import (
    DoctorSerializer,
    DoctorUpdateSerializer,
)
from .tags import doctor_tag
from pkg.schemas.tags import profile_doctor_tag


doc_doctor = extend_schema_view(
    get=extend_schema(
        tags=doctor_tag,
        summary='Список докторов',
        responses=DoctorSerializer(many=True),
        filters=None,
        parameters=[
            OpenApiParameter(
                name='page',
                type=str,
                location=OpenApiParameter.QUERY,
                description='Номер страницы'
            ),
            OpenApiParameter(
                name='limit',
                type=int,
                location=OpenApiParameter.QUERY,
                description='Количество результатов, возвращаемых на страницу'
            ),
            OpenApiParameter(
                name='ordering',
                type=str,
                location=OpenApiParameter.QUERY,
                description='''Сортировка, по рейтингу `rating`, по кол-ву отзывов `reviews`, 
                можно использовать их вместе `rating+reviews`
                - последовательность не имеет значение'''
            ),
            OpenApiParameter(
                name='search',
                type=str,
                location=OpenApiParameter.QUERY,
                description='Поиск по ФИО доктора'
            ),
            OpenApiParameter(
                name='experience',
                type=int,
                location=OpenApiParameter.QUERY,
                description='Опыт работы'
            ),
            OpenApiParameter(
                name='category',
                type=int,
                location=OpenApiParameter.QUERY,
                description='ID категории доктора'
            ),
            OpenApiParameter(
                name='degree',
                type=int,
                location=OpenApiParameter.QUERY,
                description='ID ученной степени доктора'
            ),
            OpenApiParameter(
                name='reception',
                type=str,
                location=OpenApiParameter.QUERY,
                description='''Тип приема, частная практика `private`, в клинике `clinic`, 
                можно использовать их вместе `private+clinic`'''
            ),
            OpenApiParameter(
                name='specialtie',
                type=int,
                location=OpenApiParameter.QUERY,
                description='ID специальности'
            ),
            OpenApiParameter(
                name='gender',
                type=str,
                location=OpenApiParameter.QUERY,
                description='Пол доктора',
                enum=['male', 'female']
            )
        ]
    )
)

doc_doctor_detail = extend_schema_view(
    get=extend_schema(
        tags=doctor_tag,
        summary='Данные доктора',
        responses=DoctorSerializer
    )
)

doc_profile_doctor = extend_schema_view(
    get=extend_schema(
        tags=profile_doctor_tag,
        summary='Данные доктора',
        description='Если у даннго профиля нет роли доктора, то сервер вернет ответ 403',
        responses=DoctorSerializer
    ),
    patch=extend_schema(
        tags=profile_doctor_tag,
        summary='Обновить данные доктора',
        description='Если у даннго профиля нет роли доктора, то сервер вернет ответ 403',
        responses=DoctorUpdateSerializer,
    )
)
