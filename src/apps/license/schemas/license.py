from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.article.serializers import *
from apps.clinic.serializers import *
from apps.common.schemas.tags import doctor_tag, clinic_tag
from apps.common.schemas.tags import profile_doctor_and_clinic_tag


doc_license_doctor = extend_schema_view(
    get=extend_schema(
        tags=doctor_tag,
        summary='Список лицензий доктора'
    )
)

doc_license_clinic = extend_schema_view(
    get=extend_schema(
        tags=clinic_tag,
        summary='Список лицензий клиники'
    )
)

doc_profile_license = extend_schema_view(
    get=extend_schema(
        tags=profile_doctor_and_clinic_tag,
        summary='Список лицензий',
    ),
    post=extend_schema(
        tags=profile_doctor_and_clinic_tag,
        summary='Добавить лицензию',
    )
)

doc_profile_license_detail = extend_schema_view(
    delete=extend_schema(
        tags=profile_doctor_and_clinic_tag,
        summary='Удалить лицензию',
    )
)
