from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Surgeon
from .serializers import SurgeonSerializer
from .filters import SurgeonFilter


__all__ = ['SurgeonView']


class SurgeonView(ModelViewSet):
    queryset = Surgeon.objects.prefetch_related('ratings').all()
    serializer_class = SurgeonSerializer
    
    def list(self, request, *args, **kwargs):
        filter = SurgeonFilter(request.GET, queryset=self.get_queryset())
        serializer = self.get_serializer(filter.qs, many=True)
        return Response(serializer.data)