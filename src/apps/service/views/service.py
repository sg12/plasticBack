from rest_framework.generics import ListAPIView
from apps.service.models import Service
from apps.service.serializers import *
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from pkg.permissions import IsDoctorOrClinic
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
    

@doc_profile_service
class ProfileServiceView(ListCreateAPIView):
    queryset = Service.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsDoctorOrClinic)
    serializer_class = ServiceCreateSerializer
    result_class = ServiceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


@doc_profile_service_detail
class ProfileServiceDetailView(UpdateDestroyAPIView):
    queryset = Service.objects.all()
    permission_classes = (IsAuthenticated, IsDoctorOrClinic)
    serializer_class = ServiceUpdateSerializer
    result_class = ServiceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
