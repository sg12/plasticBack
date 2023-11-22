from rest_framework.views import APIView
from rest_framework.response import Response
from apps.clinics.models import Clinic
from apps.clinics.serializers import *
from apps.clinics.filters import ClinicFilter
from rest_framework.viewsets import ModelViewSet


__all__ = ['ClinicView']


class ClinicView(ModelViewSet):
    queryset = Clinic.objects.all()
    
    default_serializer = ClinicSerializer
    create_serializer = ClinicCreateSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return self.create_serializer
        
        return self.default_serializer
    
    def list(self, request, *args, **kwargs):
        filter = ClinicFilter(request.GET, queryset=self.get_queryset())
        serializer = self.get_serializer(filter.qs, many=True)
        return Response(serializer.data)