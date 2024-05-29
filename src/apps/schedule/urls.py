from django.urls import path
from .views import *
from apps.user.urls import PROFILE_URL, PROFILE_PK_URL


urlpatterns = [
    path(PROFILE_PK_URL + '/schedule', ScheduleView.as_view()),
    path(PROFILE_URL + '/schedule', ProfileScheduleView.as_view()),
    path(PROFILE_URL + '/schedule/<int:pk>', ProfileScheduleDetailView.as_view()),
]
