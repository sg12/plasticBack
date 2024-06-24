from rest_framework.generics import ListAPIView
from apps.location.models import District
from apps.location.serializers import DistrictSerializer
from apps.location.schemas import doc_district


@doc_district
class DistrictView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
