from django.urls import path
from .views import NotificationView, NotificationDetailView

urlpatterns = [
    path('notification/', NotificationView.as_view()),
    path('notification/<int:pk>', NotificationDetailView.as_view())
]