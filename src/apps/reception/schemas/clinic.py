from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.reception.serializers import *
from apps.client.serializers import *
from pkg.schemas.tags import profile_clinic_tag


doc_profile_reception_clinic = extend_schema_view(
    get=extend_schema(
        tags=profile_clinic_tag,
        summary='Список приемов',
        responses=ReceptionClinicSerializer
    )
)
