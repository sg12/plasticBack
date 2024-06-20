from rest_framework.generics import ListAPIView
from apps.doctor.models import Specialty
from apps.doctor.serializers import SpecialitySerializer
from apps.doctor.schemas import doc_speciality


@doc_speciality
class SpecialityView(ListAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialitySerializer
    