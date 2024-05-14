from rest_framework.generics import ListAPIView
from apps.service.models import Service
from apps.service.serializers import *
from apps.service.decorators import service_access
from django.utils.decorators import method_decorator
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from apps.service.permissions import IsDoctorOrClinic
from pkg.generics import (
    ListCreateAPIView,
    UpdateDestroyAPIView
)


@method_decorator(service_access, name='dispatch')
class GuestServiceView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__pk=self.kwargs.get('pk'))
    

class ProfileServiceView(ListCreateAPIView):
    queryset = Service.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsDoctorOrClinic)
    serializer_class = ServiceCreateSerializer
    result_class = ServiceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class ProfileServiceDetailView(UpdateDestroyAPIView):
    queryset = Service.objects.all()
    permission_classes = (IsAuthenticated, IsDoctorOrClinic)
    serializer_class = ServiceUpdateSerializer
    result_class = ServiceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
