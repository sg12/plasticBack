from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from apps.surgeons.serializers import SurgeonListSerializer, SurgeonRetrieveSerializer


doc_surgeon_list = swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter(
            name='specialtie',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
        ),
        openapi.Parameter(
            name='experience',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_NUMBER,
            description='experience >= value'
        ),
        openapi.Parameter(
            name='category',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_NUMBER,
        ),
        openapi.Parameter(
            name='academic',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_NUMBER,
        ),
        openapi.Parameter(
            name='gender',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            enum=('male', 'female'),
        ),
        openapi.Parameter(
            name='reception',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            enum=('private', 'clinic'),
        ),
        openapi.Parameter(
            name='reviews',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description='reviews >= value'
        ),
        openapi.Parameter(
            name='rating',
            in_=openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description='rating >= value'
        ),
    ],
    responses={
        200: openapi.Response('', SurgeonListSerializer(many=True)),
    }
)

doc_surgeon_retrieve_update = swagger_auto_schema(
    responses={
        200: openapi.Response('', SurgeonRetrieveSerializer),
    }
)