from django.urls import path
from .views import *
from apps.user.urls import PROFILE_URL, PROFILE_PK_URL


urlpatterns = [
    path(PROFILE_PK_URL + '/services', ServiceView.as_view()),
    path(PROFILE_URL + '/services', ProfileServiceView.as_view()),
    path(PROFILE_URL + '/services/<int:pk>', ProfileServiceDetailView.as_view())
]
