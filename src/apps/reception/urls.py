from django.urls import path
from .views import *
from apps.user.urls import PROFILE_URL


urlpatterns = [
    path(PROFILE_URL + '/client/receptions', ProfileReceptionClientView.as_view()),
    path(PROFILE_URL + '/client/receptions/<int:pk>', ProfileReceptionClientDetailView.as_view()),
    
    path(PROFILE_URL + '/doctor/receptions', ProfileReceptionDoctorView.as_view()),
    path(PROFILE_URL + '/doctor/receptions/<int:pk>', ProfileReceptionDoctorDetailView.as_view()),
    
    path(PROFILE_URL + '/clinic/receptions', ProfileReceptionClinicView.as_view()),
    path(PROFILE_URL + '/clinic/receptions/<int:pk>', ProfileReceptionClientDetailView.as_view())
]
