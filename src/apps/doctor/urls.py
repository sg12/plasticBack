from django.urls import path, include
from .views import *
from apps.user.urls import PROFILE_URL


DOCTOR_URL = 'doctors'
DOCTOR_PK_URL = DOCTOR_URL + '/<int:pk>'

profile_doctor_urls = [
    path('', ProfileDoctorView.as_view()),
    path('/educations', ProfileEducationView.as_view()),
    path('/educations/<int:pk>', ProfileEducationDetailView.as_view()),
    path('/qualifications', ProfileQualificationView.as_view()),
    path('/qualifications/<int:pk>', ProfileQualificationDetailView.as_view()),
    path('/workplaces', ProfileWorkplaceView.as_view()),
    path('/workplaces/<int:pk>', ProfileWorkplaceDetailView.as_view()),
]

urlpatterns = [
    # Guest
    path(DOCTOR_URL + '/categories', CategoryView.as_view()),
    path(DOCTOR_URL + '/degree', DegreeView.as_view()),
    path(DOCTOR_URL + '/specialities', SpecialityView.as_view()),
    
    path(DOCTOR_URL, DoctorView.as_view()),
    path(DOCTOR_PK_URL, DoctorDetailView.as_view()),
    path(DOCTOR_PK_URL + '/educations', EducationView.as_view()),
    path(DOCTOR_PK_URL + '/qualifications', QualificationView.as_view()),
    path(DOCTOR_PK_URL + '/workplaces', WorkplaceView.as_view()),
    
    # Profile
    path(PROFILE_URL + '/doctor', include(profile_doctor_urls))
]
