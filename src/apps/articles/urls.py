from django.urls import path, include
from .views import *


urlpatterns = [
    path('articles/', ArticleListView.as_view()),
    path('articles/<int:pk>/', ArticleRetrieveView.as_view()),
]
