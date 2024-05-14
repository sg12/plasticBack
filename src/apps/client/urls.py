from django.urls import path
from .views import *


urlpatterns = [
    path('client/', GuestClientView.as_view())
]
