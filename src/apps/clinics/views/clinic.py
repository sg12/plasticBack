from rest_framework.views import APIView
from rest_framework.response import Response
from apps.clinics.models import Clinic
from apps.clinics.serializers import *
from apps.clinics.filters import ClinicFilter


__all__ = [
    'ClinicDetailView',
    'ClinicListView',
    'ClinicCreateView'
]


class ClinicDetailView(APIView):
    def get(self, request, pk):
        clinic = Clinic.objects.get(id=pk)
        serializer = ClinicDetailSerializer(clinic)
        return Response(serializer.data)
    

class ClinicListView(APIView):
    def get(self, request):
        filter = ClinicFilter(request.GET, queryset=Clinic.objects.all())
        serializer = ClinicDetailSerializer(filter.qs, many=True)
        return Response(serializer.data)