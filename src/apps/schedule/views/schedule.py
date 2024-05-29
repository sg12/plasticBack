from rest_framework.generics import ListAPIView
from pkg.generics import (
    ListCreateAPIView,
    UpdateDestroyAPIView
)
from apps.schedule.models import Schedule
from apps.schedule.serializers import *
from apps.doctor.permissions import IsDoctor


class ScheduleView(ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(user__pk=pk)
    

class ProfileScheduleView(ListCreateAPIView):
    queryset = Schedule.objects.all()
    permission_classes = (IsDoctor,)
    serializer_class = ScheduleCreateSerializer
    result_class = ScheduleSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class ProfileScheduleDetailView(UpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    permission_classes = (IsDoctor,)
    serializer_class = ScheduleUpdateSerializer
    result_class = ScheduleSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
