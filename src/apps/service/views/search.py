from rest_framework.generics import ListAPIView
from apps.clinic.models import Clinic
from apps.doctor.models import Doctor
from apps.service.serializers import *
from apps.clinic.serializers import ClinicSerializer
from apps.doctor.serializers import DoctorSerializer
from apps.service.models import Specialty
from django.shortcuts import get_object_or_404


class SearchDoctorsBySpecialtyView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        queryset = queryset.filter(services__specialty__pk=pk)
    

class SearchClinicsBySpecialtyView(ListAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        speciality = get_object_or_404(Specialty, pk=pk)
        
        return queryset.objects.filter(doctors__services__specialty=speciality).distinct()
