from django.urls import path
from .views import *


urlpatterns = [
    path('account/service/', AccountServiceListView.as_view()),
    path('account/service/<int:pk>/', AccountServiceRetrieveUpdateDeleteView.as_view()),
]