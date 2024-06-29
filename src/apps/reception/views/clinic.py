from rest_framework.generics import ListAPIView
from apps.reception.models import Reception
from apps.reception.serializers import *
from apps.clinic.permissions import IsClinic
from rest_framework.permissions import IsAuthenticated
from apps.reception.schemas import *


@doc_profile_reception_clinic
class ProfileReceptionClinicView(ListAPIView):
    permission_classes = (IsAuthenticated, IsClinic)
    queryset = Reception.objects.all()
    serializer_class = ReceptionClinicSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(service__user__doctor__clinic=self.request.user.clinic)
