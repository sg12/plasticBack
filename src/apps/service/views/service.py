from rest_framework.generics import ListAPIView
from apps.service.models import Service
from apps.service.serializers import *
from rest_framework.permissions import IsAuthenticated
from apps.doctor.permissions import IsDoctor
from apps.clinic.permissions import IsClinic
from rest_framework.generics import ListAPIView
from pkg.generics import (
    ListCreateAPIView,
    UpdateDestroyAPIView
)
from apps.service.schemas import *
from pkg.decorators import is_doctor_or_clinic


@is_doctor_or_clinic
class BaseServiceView(ListAPIView):
    queryset = Service.objects.order_by('-id')
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(user_id=pk)


@doc_doctor_service
class DoctorServiceView(BaseServiceView):
    pass    


@doc_clinic_service
class ClinicServiceView(BaseServiceView):
    pass
    

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
