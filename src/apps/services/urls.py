from django.urls import path, include
from .views import *


urlpatterns = [
    path('services/', ServiceInfoListView.as_view()),
    # path('services/<slug:slug>/', SearchClinicByServiceSlugView.as_view()), # Refactor
]
