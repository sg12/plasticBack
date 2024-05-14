from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from apps.doctor.serializers import (
    DoctorSerializer,
    DoctorUpdateSerializer,
)

tags = ['doctor']

doc_doctor = extend_schema_view(
    get=extend_schema(
        tags=tags,
        responses=DoctorSerializer(many=True),
    )
)


doc_doctor_detail = extend_schema_view(
    get=extend_schema(
        tags=tags,
        responses=DoctorSerializer,
    ),
    patch=extend_schema(
        tags=tags,
        responses=DoctorUpdateSerializer,
    )
)
