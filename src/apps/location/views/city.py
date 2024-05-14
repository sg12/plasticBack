from rest_framework.generics import ListAPIView
from apps.location.models import City
from apps.location.serializers import CitySerializer
from apps.location.schemas import doc_metro


@doc_metro
class CityView(ListAPIView):
    queryset = City
    serializer_class = CitySerializer
