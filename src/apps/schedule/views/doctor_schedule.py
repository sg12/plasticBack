from rest_framework.generics import ListAPIView
from pkg.generics import (
    ListCreateAPIView,
    UpdateDestroyAPIView
)
from apps.schedule.models import DoctorSchedule
from apps.schedule.serializers import *


class DoctorScheduleView(ListAPIView):
    queryset = DoctorSchedule.objects.all()
    serializer_class = DoctorScheduleSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(user__pk=pk)
    

class ProfileDoctorScheduleView(ListCreateAPIView):
    queryset = DoctorSchedule.objects.all()
    serializer_class = DoctorScheduleCreateSerializer
    result_class = DoctorScheduleSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class ProfileDoctorScheduleView(UpdateDestroyAPIView):
    queryset = DoctorSchedule.objects.all()
    serializer_class = DoctorScheduleUpdateSerializer
    result_class = DoctorScheduleSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
