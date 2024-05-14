from rest_framework.generics import ListAPIView
from apps.location.models import Metro
from apps.location.serializers import MetroSerializer
from apps.location.schemas import doc_city


@doc_city
class MetroView(ListAPIView):
    queryset = Metro
    serializer_class = MetroSerializer
