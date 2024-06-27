from django.urls import path
from .views import *


urlpatterns = [
    path('faq', FAQListView.as_view()),
]
