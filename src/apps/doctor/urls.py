from django.urls import path
from .views import *


urlpatterns = [
    path('doctors/', DoctorView.as_view()),
    path('doctors/<int:pk>/', DoctorDetailView.as_view()),
    path('doctors/<int:pk>/services/', DoctorServiceView.as_view()),
]
