from django.urls import path
from .views import *
from apps.user.urls import PROFILE_URL
from apps.doctor.urls import DOCTOR_PK_URL
from apps.clinic.urls import CLINIC_PK_URL


urlpatterns = [
    # Guest
    path(DOCTOR_PK_URL + '/licenses', LicenseDoctorView.as_view()),
    path(CLINIC_PK_URL + '/licenses', LicenseClinicView.as_view()),
    
    # Profile
    path(PROFILE_URL + '/licenses', ProfileLicenseView.as_view()),
    path(PROFILE_URL + '/licenses/<int:pk>', ProfileLicenseDetailView.as_view()),
]
