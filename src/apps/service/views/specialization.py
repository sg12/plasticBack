from rest_framework.generics import ListAPIView
from apps.service.models import Specialization
from apps.service.serializers import SpecializationSerializer
from apps.service.schemas import *


@doc_specialization
class SpecializationView(ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
