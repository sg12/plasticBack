from django.urls import path
from .views import *
from apps.user.urls import PROFILE_URL


FAVORITY_URL = PROFILE_URL + '/client/favorities'
FAVORITY_PK_URL = FAVORITY_URL + '/<int:pk>'

urlpatterns = [
    path(FAVORITY_URL + '/doctors', FavoriteDoctorView.as_view()),
    path(FAVORITY_URL + '/clinics', FavoriteClinicView.as_view()),
    path(FAVORITY_URL, AddFavoriteView.as_view()),
    path(FAVORITY_PK_URL, FavoriteDetailView.as_view()),
]
