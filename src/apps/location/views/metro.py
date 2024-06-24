from rest_framework.generics import ListAPIView
from apps.location.models import Metro
from apps.location.serializers import MetroSerializer
from apps.location.schemas import doc_metro


@doc_metro
class MetroView(ListAPIView):
    queryset = Metro.objects.all()
    serializer_class = MetroSerializer
