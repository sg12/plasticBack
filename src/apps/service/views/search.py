from rest_framework.generics import ListAPIView
from apps.clinic.models import Clinic
from apps.doctor.models import Doctor
from apps.service.serializers import *
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch
from apps.service.models import Service
from pkg.pagination import PagePagination


class SearchDoctorServiceView(ListAPIView):
    queryset = Service.objects.all()
    pagination_class = PagePagination
    serializer_class = DoctorServiceSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related(Prefetch(
            'doctor',
            queryset=Doctor.objects.all()
        ))
        
        pk = self.kwargs.get('pk')
        return queryset.filter(specialty__pk=pk)
    

class SearchClinicServiceView(ListAPIView):
    queryset = Service.objects.all()
    pagination_class = PagePagination
    serializer_class = ClinicServiceSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        
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
        
        return queryset.filter(specialty__pk=pk).exclude(doctor__clinic=None)
