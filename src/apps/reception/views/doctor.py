from rest_framework.generics import ListAPIView
from pkg.generics import UpdateDestroyAPIView
from apps.reception.models import Reception
from apps.reception.serializers import *
from apps.doctor.permissions import IsDoctor
from rest_framework.permissions import IsAuthenticated
from apps.reception.schemas import *


@doc_profile_reception_doctor
class ProfileReceptionDoctorView(ListAPIView):
    queryset = Reception.objects.all()
    permission_classes = (IsAuthenticated, IsDoctor)
    serializer_class = ReceptionDoctorSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(service__user=self.request.user)


@doc_profile_reception_doctor_detail
class ProfileReceptionDoctorDetailView(UpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsDoctor)
    queryset = Reception.objects.all()
    serializer_class = ReceptionDoctorUpdateSerializer
    result_class = ReceptionDoctorSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(
            service__user=self.request.user,
            pk=pk
        )

