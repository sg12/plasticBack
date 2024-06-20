from rest_framework.generics import ListAPIView
from apps.service.models import Specialization
from apps.service.serializers import *
from apps.service.schemas import *


class SpecializationView(ListAPIView):
    queryset = Specialization.objects.all()
    serializer_class = ServiceSerializer
