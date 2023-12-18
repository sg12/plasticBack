from django.urls import path, include
from .views import *


urlpatterns = [
    path('services/', ServiceListView.as_view()),
    path('services/<slug:slug>/', ServiceSlugView.as_view()),
]
