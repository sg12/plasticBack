from rest_framework.generics import ListAPIView
from pkg.generics import ListCreateAPIView, UpdateDestroyAPIView
from apps.doctor.serializers import *
from apps.doctor.models import Education
from rest_framework.permissions import IsAuthenticated
from apps.doctor.permissions import IsDoctor
from django.shortcuts import get_object_or_404


class EducationView(ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(doctor__pk=pk)
    

class ProfileEducationView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsDoctor)
    queryset = Education.objects.all()
    serializer_class = EducationCreateSerializer
    result_class = EducationSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(doctor=self.request.user.doctor)
    

class ProfileEducationDetailView(UpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsDoctor)
    queryset = Education.objects.all()
    serializer_class = EducationUpdateSerializer
    result_class = EducationSerializer
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        doctor = self.request.user.doctor
        return get_object_or_404(
            self.queryset.model, 
            doctor=doctor,
            pk=pk
        )
