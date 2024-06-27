from drf_spectacular.utils import extend_schema_view, extend_schema
from apps.schedule.serializers import DoctorScheduleSerializer
from pkg.schemas.tags import review_tag


doc_doctor_schedule = extend_schema_view(
    get=extend_schema(
        tags=review_tag,
        summary='Рабочее расписание',
        responses=DoctorScheduleSerializer(many=True)
    )
)
