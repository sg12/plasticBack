from rest_framework.generics import ListAPIView, DestroyAPIView
from apps.reception.models import Reception
from apps.reception.serializers import *
from apps.clinic.permissions import IsClinic
from rest_framework.permissions import IsAuthenticated
from apps.reception.schemas import *


@doc_profile_reception_doctor
class ProfileReceptionDoctorView(ListAPIView):
    permission_classes = (IsAuthenticated, IsClinic)
    queryset = Reception.objects.all()
    serializer_class = ReceptionDoctorSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(doctor=self.request.user.doctor)


@doc_profile_reception_doctor_detail
class ProfileReceptionDoctorDetailView(DestroyAPIView):
    permission_classes = (IsAuthenticated, IsClinic)
    queryset = Reception.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(
            doctor=self.request.user.doctor,
            pk=pk
        )

