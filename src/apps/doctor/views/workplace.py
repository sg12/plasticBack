from rest_framework.generics import ListAPIView
from pkg.generics import ListCreateAPIView, UpdateDestroyAPIView
from apps.doctor.serializers import *
from apps.doctor.models import Workplace
from rest_framework.permissions import IsAuthenticated
from apps.doctor.permissions import IsDoctor
from django.shortcuts import get_object_or_404


class GuestWorkplaceView(ListAPIView):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(doctor__pk=pk)
    

class ProfileWorkplaceView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsDoctor)
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceCreateSerializer
    result_class = WorkplaceSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(doctor=self.request.user.doctor)
    

class ProfileWorkplaceDetailView(UpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsDoctor)
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceUpdateSerializer
    result_class = WorkplaceSerializer
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        doctor = self.request.user.doctor
        return get_object_or_404(
            self.queryset.model, 
            doctor=doctor,
            pk=pk
        )
