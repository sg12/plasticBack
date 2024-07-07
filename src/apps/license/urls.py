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
    path(PROFILE_URL + '/doctor/licenses', ProfileDoctorLicenseView.as_view()),
    path(PROFILE_URL + '/doctor/licenses/<int:pk>', ProfileDoctorLicenseDetailView.as_view()),
    
    path(PROFILE_URL + '/clinic/licenses', ProfileClinicLicenseView.as_view()),
    path(PROFILE_URL + '/clinic/licenses/<int:pk>', ProfileClinicLicenseDetailView.as_view()),
]
