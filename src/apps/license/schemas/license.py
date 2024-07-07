from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.article.serializers import *
from apps.clinic.serializers import *
from apps.license.serializers import LicenseSerializer, LicenseCreateSerializer
from pkg.schemas.tags import (
    doctor_tag, 
    clinic_tag, 
    profile_doctor_tag,
    profile_clinic_tag
)


doc_license_doctor = extend_schema_view(
    get=extend_schema(
        tags=doctor_tag,
        summary='Список лицензий доктора',
        responses=LicenseSerializer
    )
)

doc_license_clinic = extend_schema_view(
    get=extend_schema(
        tags=clinic_tag,
        summary='Список лицензий клиники',
        responses=LicenseSerializer
    )
)

doc_profile_doctor_license = extend_schema_view(
    get=extend_schema(
        tags=profile_doctor_tag,
        summary='Список лицензий',
        responses=LicenseSerializer
    ),
    post=extend_schema(
        tags=profile_doctor_tag,
        summary='Добавить лицензию',
        request=LicenseCreateSerializer,
        responses=LicenseSerializer
    )
)

doc_profile_doctor_license_detail = extend_schema_view(
    delete=extend_schema(
        tags=profile_doctor_tag,
        summary='Удалить лицензию'
    )
)

doc_profile_clinic_license = extend_schema_view(
    get=extend_schema(
        tags=profile_clinic_tag,
        summary='Список лицензий',
        responses=LicenseSerializer
    ),
    post=extend_schema(
        tags=profile_clinic_tag,
        summary='Добавить лицензию',
        request=LicenseCreateSerializer,
        responses=LicenseSerializer
    )
)

doc_profile_clinic_license_detail = extend_schema_view(
    delete=extend_schema(
        tags=profile_clinic_tag,
        summary='Удалить лицензию',
    )
)
