from django.urls import path
from .views import *


urlpatterns = [
    path('favorites/', FavoriteDetailView.as_view()),
]
