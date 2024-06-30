from django.urls import path
from .views import *
from apps.user.urls import PROFILE_URL
from apps.doctor.urls import DOCTOR_PK_URL
from apps.clinic.urls import CLINIC_PK_URL


urlpatterns = [
    path(DOCTOR_PK_URL + '/services', DoctorServiceView.as_view()),
    path(CLINIC_PK_URL + '/services', ClinicServiceView.as_view()),
    
    path(PROFILE_URL + '/doctor/services', ProfileDoctorServiceView.as_view()),
    path(PROFILE_URL + '/doctor/services/<int:pk>', ProfileDoctorServiceDetailView.as_view()),
    
    path(PROFILE_URL + '/clinic/services', ProfileClinicServiceView.as_view()),
    
    path(PROFILE_URL + '/services/specialities', SpecialityView.as_view()),
]
