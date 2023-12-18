from django.urls import path
from .views import *


urlpatterns = [
    path('auth/login/', LoginView.as_view()),
    path('auth/register/<path:type>/', RegisterView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
]
