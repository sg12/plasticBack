from django.urls import path
from .views import *


urlpatterns = [
    path('metro', MetroView.as_view()),
    path('districts', DistrictView.as_view()),
    path('cities', CityView.as_view()),
]
