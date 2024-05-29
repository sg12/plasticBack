from django.urls import path
from .views import *
from apps.user.urls import PROFILE_URL


CLINIC_URL = 'clinics'
CLINIC_PK_URL = CLINIC_URL + '/<int:pk>'

urlpatterns = [
    # Guest
    path(CLINIC_URL, ClinicView.as_view()),
    path(CLINIC_PK_URL, ClinicDetailView.as_view()),
    path(CLINIC_PK_URL + '/employes', EmployeView.as_view()),
    
    # Profile
    path(PROFILE_URL + '/clinic', ProfileClinicDetailView.as_view()),
    path(PROFILE_URL + '/employes', ProfileEmployeView.as_view()),
]
