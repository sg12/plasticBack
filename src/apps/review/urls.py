from django.urls import path, include
from .views import *

urlpatterns = [
    path('reviews/', ReviewView.as_view()),
    path('reviews/<int:pk>/', ReviewDetailView.as_view()),
]
