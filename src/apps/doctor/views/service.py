from apps.doctor.models import Doctor
from apps.user.models import User
from apps.service.models import Service
from apps.service.serializers import ServiceSerializer
from django.shortcuts import get_object_or_404
from pkg.generics import ListAPIView
from apps.doctor.schemas import doc_doctor_service


@doc_doctor_service
class DoctorServiceView(ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        get_object_or_404(User, pk=pk, type='doctor')
        return Service.objects.filter(user_id=pk)
