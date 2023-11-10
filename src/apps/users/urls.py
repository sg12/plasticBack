from django.urls import path, include, re_path
from .views import RegisterAPIView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('register/', RegisterAPIView.as_view())
]