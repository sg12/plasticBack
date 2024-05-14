from rest_framework.generics import ListAPIView
from pkg.generics import (
    ListCreateAPIView,
    UpdateDestroyAPIView
)
from apps.schedule.models import ClinicSchedule
from apps.schedule.serializers import *


class ClinicScheduleView(ListAPIView):
    queryset = ClinicSchedule.objects.all()
    serializer_class = DoctorScheduleSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(user__pk=pk)
    

class ProfileClinicScheduleView(ListCreateAPIView):
    queryset = ClinicSchedule.objects.all()
    serializer_class = DoctorScheduleCreateSerializer
    result_class = DoctorScheduleSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class ProfileClinicScheduleView(UpdateDestroyAPIView):
    queryset = ClinicSchedule.objects.all()
    serializer_class = DoctorScheduleUpdateSerializer
    result_class = DoctorScheduleSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
