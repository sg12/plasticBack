from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from apps.clinics.models import Surgeon
from apps.clinics.serializers import SurgeonSerializer


__all__ = ['SurgeonView']


class SurgeonView(ModelViewSet):
    queryset = Surgeon.objects.all()
    serializer_class = SurgeonSerializer