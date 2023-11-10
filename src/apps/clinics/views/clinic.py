from rest_framework.views import APIView
from rest_framework.response import Response
from apps.clinics.models import Clinic
from apps.clinics.serializers import ClinicSerializer
from apps.clinics.filters import ClinicFilter
    

class ClinicDetailView(APIView):
    def get(self, request, pk):
        clinic = Clinic.objects.get(id=pk)
        serializer = ClinicSerializer(clinic)
        return Response(serializer.data)
    

class ClinicListView(APIView):
    def get(self, request):
        filter = ClinicFilter(request.GET, queryset=Clinic.objects.all())
        serializer = ClinicSerializer(filter.qs, many=True)
        return Response(serializer.data)