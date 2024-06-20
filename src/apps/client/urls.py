from django.urls import path
from .views import *
from apps.user.urls import PROFILE_URL


CLIENT_URL = 'clients'
CLIENT_PK_URL = CLIENT_URL + '/<int:pk>'

urlpatterns = [
    # Guest
    path(CLIENT_PK_URL, ClientView.as_view()),
    
    # Profile
    path(PROFILE_URL + '/client', ProfileClientView.as_view())
]
