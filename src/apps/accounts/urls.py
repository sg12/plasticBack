from django.urls import path
from .views import *

urlpatterns = [
    path('account/', AccountView.as_view()),
    path('account/services/', AccountServiceListCreateView.as_view()),
    path('account/services/<int:pk>/', AccountServiceRetrieveUpdateDeleteView.as_view()),
]
