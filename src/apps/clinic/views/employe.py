from rest_framework.generics import ListAPIView
from apps.doctor.models import Doctor
from apps.clinic.serializers import EmployeDoctorSerializer
from rest_framework.permissions import IsAuthenticated
from apps.clinic.permissions import IsClinic
from apps.clinic.schemas import *
from pkg.decorators import is_clinic


@doc_employe
@is_clinic
class EmployeView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = EmployeDoctorSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(clinic__user_id=pk)
    

@doc_profile_employe
class ProfileEmployeView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = EmployeDoctorSerializer
    permission_classes = (IsAuthenticated, IsClinic)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(clinic__user=self.request.user)
