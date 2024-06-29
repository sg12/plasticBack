from django.urls import path
from .views import *


urlpatterns = [
    path('tickets', TicketView.as_view()),
    path('tickets/<int:pk>', TicketDetailView.as_view()),
    path('tickets/<int:pk>/messages', MessageView.as_view()),
    path('tickets/messages/<int:pk>', MessageDetailView.as_view())
]
