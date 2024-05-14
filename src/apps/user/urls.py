from django.urls import path, include
from apps.client import *
from .views import *


BASE_PROFILE_URL = 'profile'
BASE_USER_URL = 'user/<int:pk>'

urlpatterns = [
    path(BASE_PROFILE_URL, MeView.as_view())
    # path('user', ),
    # path('user/<int:pk>', )
]
