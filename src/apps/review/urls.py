from django.urls import path
from .views import *
from apps.doctor.urls import DOCTOR_PK_URL
from apps.clinic.urls import CLINIC_PK_URL


urlpatterns = [
    path(DOCTOR_PK_URL + '/reviews', ReviewDoctorView.as_view()),
    path(CLINIC_PK_URL + '/reviews', ReviewClinicView.as_view()),
    path('reviews/<int:pk>', ReviewDetailView.as_view()),
    path('reviews/<int:pk>/replies', ReplyView.as_view())
]
