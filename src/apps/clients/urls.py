from django.urls import path, include
from .views import *


urlpatterns = [
    path('clients/<int:pk>/', ClientRetrieveView.as_view()),
]
