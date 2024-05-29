from rest_framework.generics import ListAPIView, DestroyAPIView
from apps.reception.models import Reception
from apps.reception.serializers import *
from apps.doctor.permissions import IsDoctor
from rest_framework.permissions import IsAuthenticated


class ProfileReceptionClinicView(ListAPIView):
    permission_classes = (IsAuthenticated, IsDoctor)
    queryset = Reception.objects.all()
    serializer_class = ReceptionClientSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(doctor__clinic=self.request.user.clinic)


class ProfileReceptionClinicDetailView(DestroyAPIView):
    permission_classes = (IsAuthenticated, IsDoctor)
    queryset = Reception.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(
            doctor__clinic=self.request.user.clinic,
            pk=pk
        )

