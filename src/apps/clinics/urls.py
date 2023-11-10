from django.urls import path
from .views import ClinicListView

urlpatterns = [
    path('clinics/', ClinicListView.as_view()),
]
