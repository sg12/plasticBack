from rest_framework.generics import ListAPIView
from apps.service.models import Service
from apps.user.models import User
from apps.service.serializers import *
from rest_framework.permissions import IsAuthenticated
from apps.doctor.permissions import IsDoctor
from rest_framework.generics import ListAPIView
from pkg.generics import (
    ListCreateAPIView,
    UpdateDestroyAPIView
)
from apps.service.schemas import *
from pkg.decorators import is_doctor, is_clinic


@doc_doctor_service
@is_doctor
class DoctorServiceView(ListAPIView):
    queryset = Service.objects.order_by('-id')
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(user_id=pk)


@doc_clinic_service
@is_clinic
class ClinicServiceView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        
        pk = self.kwargs.get('pk')
        user = User.objects.get(pk=pk)
        employes = user.clinic.employes.all()
        
        return queryset.filter(user__doctor__in=employes).distinct()
    

@doc_profile_doctor_service
class ProfileDoctorServiceView(ListCreateAPIView):
    queryset = Service.objects.all()
    permission_classes = (IsAuthenticated, IsDoctor)
    serializer_class = ServiceCreateSerializer
    result_class = ServiceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


@doc_profile_doctor_service_detail
class ProfileDoctorServiceDetailView(UpdateDestroyAPIView):
    queryset = Service.objects.all()
    permission_classes = (IsAuthenticated, IsDoctor)
    serializer_class = ServiceUpdateSerializer
    result_class = ServiceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


@doc_profile_clinic_service
class ProfileClinicServiceView(ProfileDoctorServiceView):
    http_method_names = ['get']
