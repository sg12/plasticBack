from django.urls import path
from .views import *


urlpatterns = [
    path('clinics/', ClinicListView.as_view()),
    path('clinics/<int:pk>/', ClinicRetrieveUpdateView.as_view()),
    path('clinics/<int:pk>/services/', ClinicServiceListView.as_view()),

    path('metro/', MetroListView.as_view()),
    path('district/', DistrictListView.as_view()),

    # Rework
    # path('clinics/<int:clinic_id>/review/', ReviewListCreateView.as_view()),
    # path('clinics/<int:clinic_id>/review/<int:review_id>/', RetrieveUpdateDestroyAPIView.as_view()),
]
