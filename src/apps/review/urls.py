from django.urls import path
from .views import *
from apps.user.urls import PROFILE_PK_URL


urlpatterns = [
    path(PROFILE_PK_URL + '/reviews', ReviewView.as_view()),
    path(PROFILE_PK_URL + '/reviews/<int:pk>', ReviewDetailView.as_view()),
    
    path('reviews/<int:review_pk>/replies', ReplyView.as_view()),
    path('replies/<int:pk>', ReplyDetailView.as_view())
]
