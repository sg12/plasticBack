from rest_framework.generics import ListAPIView
from pkg.generics import (
    ListCreateAPIView,
    UpdateDestroyAPIView
)
from apps.schedule.models import ClinicSchedule
from apps.schedule.serializers import *
from apps.clinic.permissions import IsClinic


class ClinicScheduleView(ListAPIView):
    queryset = ClinicSchedule.objects.all()
    permission_classes = (IsClinic,)
    serializer_class = ClinicScheduleSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user_pk = self.kwargs.get('user_pk')
        return queryset.filter(user__pk=user_pk)
    

class ProfileClinicScheduleView(ListCreateAPIView):
    queryset = ClinicSchedule.objects.all()
    permission_classes = (IsClinic,)
    serializer_class = ClinicScheduleCreateSerializer
    result_class = ClinicScheduleSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class ProfileClinicScheduleDetailView(UpdateDestroyAPIView):
    queryset = ClinicSchedule.objects.all()
    permission_classes = (IsClinic,)
    serializer_class = ClinicScheduleUpdateSerializer
    result_class = ClinicScheduleSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
