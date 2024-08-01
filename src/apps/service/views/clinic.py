from rest_framework.generics import ListAPIView
from apps.service.models import Service
from apps.user.models import User
from apps.service.serializers import *
from rest_framework.permissions import IsAuthenticated
from apps.clinic.permissions import IsClinic
from rest_framework.generics import ListAPIView
from apps.service.schemas import *
from pkg.decorators import is_clinic


@doc_clinic_service
@is_clinic
class ClinicServiceView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        
        pk = self.kwargs.get('pk')
        user = User.objects.get(pk=pk)
        employes = user.clinic_employes.all()
        
        return queryset.filter(doctor__in=employes).distinct()


@doc_profile_clinic_service
class ProfileClinicServiceView(ListAPIView):
    queryset = Service.objects.all()
    permission_classes = (IsAuthenticated, IsClinic)
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        employes = self.request.user.clinic_employes.all()
        
        return queryset.filter(doctor__in=employes).distinct()
