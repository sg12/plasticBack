from rest_framework.generics import ListAPIView
from apps.clinic.models import Clinic
from apps.doctor.models import Doctor
from apps.service.models import Specialty
from apps.service.serializers import *
from django.db.models import Prefetch
from apps.service.models import Service
from pkg.pagination import PagePagination
from django.shortcuts import get_object_or_404
from apps.service.schemas import (
    doc_search_doctor_service,
    doc_search_clinic_service
)


@doc_search_doctor_service
class SearchDoctorServiceView(ListAPIView):
    queryset = Service.objects.all()
    pagination_class = PagePagination
    serializer_class = DoctorServiceSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        specialty = get_object_or_404(Specialty, pk=pk)
        
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related(Prefetch(
            'doctor',
            queryset=Doctor.objects.all()
        ))
        
        return queryset.filter(specialty=specialty)
    

@doc_search_clinic_service
class SearchClinicServiceView(ListAPIView):
    queryset = Service.objects.all()
    pagination_class = PagePagination
    serializer_class = ClinicServiceSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        specialty = get_object_or_404(Specialty, pk=pk)
        
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related(
            Prefetch(
                'doctor',
                queryset=Doctor.objects.all(),
            ),
            Prefetch(
                'doctor__clinic',
                queryset=Clinic.objects.all(),
            )
        )
        
        return queryset.filter(specialty=specialty).exclude(doctor__clinic=None)
