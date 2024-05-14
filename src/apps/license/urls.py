from django.urls import path
from .views import *
from apps.user.urls import BASE_PROFILE_URL, BASE_USER_URL


urlpatterns = [
    # Guest
    path(BASE_USER_URL + '/licenses', LicenseView.as_view()),
    
    # Profile
    path(BASE_PROFILE_URL + '/licenses', ProfileLicenseView.as_view()),
    path(BASE_PROFILE_URL + '/licenses/<int:pk>', ProfileLicenseDetailView.as_view()),
]
