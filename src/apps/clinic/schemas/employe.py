from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.article.serializers import *
from apps.clinic.serializers import *
from pkg.schemas.tags import clinic_tag, profile_clinic_tag


doc_employe = extend_schema_view(
    get=extend_schema(
        summary='Возвращает список работников клиники',
        tags=clinic_tag,
    )
)

doc_profile_employe = extend_schema_view(
    get=extend_schema(
        summary='Возвращает список работников клиники',
        tags=profile_clinic_tag,
    )
)
