from django.urls import path
from .views import *


FAVORITY_URL = 'favorities'

urlpatterns = [
    path(FAVORITY_URL, FavoriteView.as_view()),
    path(FAVORITY_URL, FavoriteDetailView.as_view()),
]
