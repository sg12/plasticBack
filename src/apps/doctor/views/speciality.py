from rest_framework.generics import ListAPIView
from apps.doctor.models import Specialty
from apps.doctor.serializers import SpecialitySerializer


class SpecialityView(ListAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialitySerializer
    