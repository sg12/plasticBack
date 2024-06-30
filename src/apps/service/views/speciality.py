from rest_framework.generics import ListAPIView
from apps.service.models import Specialty
from apps.service.serializers import SpecialitySerializer
from apps.service.schemas import doc_speciality


@doc_speciality
class SpecialityView(ListAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialitySerializer
    