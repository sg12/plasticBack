from django.urls import path
from .views import GetStatyi

urlpatterns = [
    path('statiy/', GetStatyi.as_view())
]
