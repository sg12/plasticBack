from django.urls import path, include
from .views import *


urlpatterns = [
    path('articles/', ArticleReadView.as_view()),
    path('articles/<int:pk>/', ArticleReadView.as_view()),
    
    path('articles/categoryes/', CategoryReadView.as_view()),
]
