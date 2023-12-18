from django.urls import path
from .views import *

urlpatterns = [
    path('users/me/', UserMeView.as_view()),
]
