from rest_framework.generics import ListAPIView
from apps.service.models import Service
from apps.service.serializers import *
from apps.service.decorators import service_access
from django.utils.decorators import method_decorator
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


@method_decorator(service_access, name='dispatch')
class BaseServiceView(ListAPIView):
    permission_classes = (IsDoctorOrClinic,)
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_pk = self.kwargs.get('user_pk')
        return queryset.filter(user__pk=user_pk)


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
