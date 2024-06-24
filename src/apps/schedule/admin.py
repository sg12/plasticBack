from django.contrib import admin
from apps.schedule.models import (
    ClinicSchedule,
    DoctorSchedule,
    Schedule,
    Weekday
)

admin.site.register([
    ClinicSchedule, 
    DoctorSchedule,
    Schedule,
    Weekday
])
