from django.urls import path, include
from apps.client import *
from .views import *

PROFILE_URL = 'profile'
PROFILE_PK_URL = PROFILE_URL + '/<int:user_pk>'


urlpatterns = [
    path(PROFILE_URL, MeView.as_view())
]
