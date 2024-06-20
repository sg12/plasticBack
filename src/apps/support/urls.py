from django.urls import path
from .views import *


urlpatterns = [
    path('tickets', TicketView.as_view()),
    path('tickets/<int:ticket_id>', TicketDetailView.as_view()),
    path('tickets/<int:ticket_id>/messages', MessageView.as_view()),
    path('tickets/messages/<int:msg_id>', MessageDetailView.as_view())
]
