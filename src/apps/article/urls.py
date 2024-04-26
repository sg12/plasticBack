from django.urls import path
from .views import ArticleView, ArticleDetailView


urlpatterns = [
    path('article/', ArticleView.as_view()),
    path('article/<int:pk>', ArticleDetailView.as_view())
]