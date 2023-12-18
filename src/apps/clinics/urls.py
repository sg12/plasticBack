from django.urls import path
from .views import *


urlpatterns = [
    path('clinics/<int:pk>/rating', RatingView.as_view()),
    
    path('clinics/', ClinicListView.as_view()),
    path('clinics/<int:pk>/', ClinicRetrieveView.as_view()),
    
    path('metro/', MetroListView.as_view()),
    path('district/', DistrictListView.as_view()),
]
