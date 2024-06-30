from rest_framework.generics import ListAPIView
from apps.doctor.models import Specialization
from apps.service.serializers import *
from apps.doctor.schemas import *


@doc_dspecialization
class SpecializationView(ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = ServiceSerializer
