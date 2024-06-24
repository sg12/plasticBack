from rest_framework.generics import ListAPIView
from apps.location.models import City
from apps.location.serializers import CitySerializer
from apps.location.schemas import doc_city


@doc_city
class CityView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
