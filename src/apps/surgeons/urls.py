from django.urls import path
from .views import *


urlpatterns = [
    path('surgeons/', SurgeonListView.as_view()),
    path('surgeons/<int:pk>/', SurgeonRetrieveUpdateView.as_view()),
    path('surgeons/<int:pk>/services/', SurgeonServiceListView.as_view()),
]
