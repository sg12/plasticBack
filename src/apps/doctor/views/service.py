from apps.service.models import Service
from apps.service.serializers import ServiceSerializer
from pkg.generics import ListAPIView
from apps.doctor.schemas import doc_doctor_service
from apps.doctor.permissions import IsDoctor


@doc_doctor_service
class DoctorServiceView(ListAPIView):    
    serializer_class = ServiceSerializer
    permission_classes = (IsDoctor,)

    def get_queryset(self):
        user_pk = self.kwargs.get('pk')
        return Service.objects.filter(user__pk=user_pk)
