from rest_framework.generics import ListAPIView
from apps.doctor.models import Specialization
from apps.doctor.serializers import SpecializationSerializer
from apps.doctor.schemas import *


@doc_specialization
class SpecializationView(ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
