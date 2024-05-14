from rest_framework.generics import ListAPIView
from apps.doctor.models import Degree
from apps.doctor.serializers import DegreeSerializer


class DegreeView(ListAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
