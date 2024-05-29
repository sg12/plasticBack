from django.urls import path
from .views import *
from apps.user.urls import PROFILE_URL


DOCTOR_URL = 'doctors'
DOCTOR_PK_URL = DOCTOR_URL + '/<int:pk>'

urlpatterns = [
    # Guest
    path(DOCTOR_URL + '/categories', CategoryView.as_view()),
    path(DOCTOR_URL + '/degree', DegreeView.as_view()),
    path(DOCTOR_URL + '/specialities', SpecialityView.as_view()),
    
    path(DOCTOR_URL, DoctorView.as_view()),
    path(DOCTOR_PK_URL, DoctorDetailView.as_view()),
    path(DOCTOR_PK_URL + '/services', DoctorServiceView.as_view()),
    path(DOCTOR_PK_URL + '/educations', EducationView.as_view()),
    path(DOCTOR_PK_URL + '/qualifications', QualificationView.as_view()),
    path(DOCTOR_PK_URL + '/workplaces', WorkplaceView.as_view()),
    
    # Profile
    path(PROFILE_URL + '/doctor', ProfileDoctorView.as_view()),
    path(PROFILE_URL + '/educations', ProfileEducationView.as_view()),
    path(PROFILE_URL + '/educations/<int:pk>', ProfileEducationDetailView.as_view()),
    path(PROFILE_URL + '/qualifications', ProfileQualificationView.as_view()),
    path(PROFILE_URL + '/qualifications/<int:pk>', ProfileQualificationDetailView.as_view()),
    path(PROFILE_URL + '/workplaces', ProfileWorkplaceView.as_view()),
    path(PROFILE_URL + '/workplaces/<int:pk>', ProfileWorkplaceDetailView.as_view()),
]
