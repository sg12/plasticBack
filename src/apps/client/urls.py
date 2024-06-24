from django.urls import path
from .views import *
from apps.user.urls import PROFILE_URL


urlpatterns = [
    # Guest
    path('clients/<int:pk>', ClientView.as_view()),
    
    # Profile
    path(PROFILE_URL + '/client', ProfileClientView.as_view())
]
