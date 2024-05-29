from django.urls import path
from .views import *
from apps.user.urls import PROFILE_URL

CLIENT_URL = 'clients'
CLIENT_PK_URL = CLIENT_URL + '/<int:pk>'

urlpatterns = [
    # Guest
    path(CLIENT_PK_URL, GuestClientView.as_view()),
    
    # Profile
    path(PROFILE_URL, ProfileClientView.as_view())
]
