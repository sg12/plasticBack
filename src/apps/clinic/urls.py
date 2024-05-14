from django.urls import path
from .views import *
from apps.user.urls import BASE_PROFILE_URL


BASE_CLINIC_URL = 'clinics'
CLINIC_PK = BASE_CLINIC_URL + '/<int:pk>'

urlpatterns = [
    # Guest
    path(BASE_CLINIC_URL, ClinicView.as_view()),
    path(CLINIC_PK, ClinicDetailView.as_view()),
    path(CLINIC_PK + '/employes', EmployeView.as_view()),
    
    # Profile
    path(BASE_PROFILE_URL + '/clinic', ProfileClinicDetailView.as_view()),
    path(BASE_PROFILE_URL + '/employes', ProfileEmployeView.as_view()),
]
