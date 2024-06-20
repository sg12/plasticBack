from rest_framework.generics import ListAPIView
from apps.doctor.models import Degree
from apps.doctor.serializers import DegreeSerializer
from apps.doctor.schemas import doc_degree


@doc_degree
class DegreeView(ListAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer
