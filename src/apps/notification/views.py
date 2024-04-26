from rest_framework.views import APIView
from .models import Notification
from .serializers import NotificationSerializer, NotificationCreateSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from .yasg import *
from django.utils.decorators import method_decorator


@method_decorator(doc_notification_list, name="get")
@method_decorator(doc_notification_create, name="post")
class NotificationView(ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationCreateSerializer


class NotificationDetailView(DestroyAPIView):
    queryset = Notification.objects.all()



    

        


    




