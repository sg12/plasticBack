from django.urls import path
from .views import *


urlpatterns = [
    path('tickets', TicketView.as_view()),
    path('tickets/<int:pk>', TicketDetailView.as_view()),
    path('tickets/answers', AnswerView.as_view()),
    path('tickets/answers/<int:pk>', AnswerDetailView.as_view())
]
