from rest_framework.response import Response
from apps.clinics.models import Clinic
from apps.clinics.serializers import *
from apps.clinics.filters import ClinicFilter
from apps.surgeons.models import Surgeon
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import Http404
from apps.clinics.yasg import *


__all__ = (
    'ClinicListView',
    'ClinicRetrieveView'
)


class ClinicListView(APIView):
    @doc_clinic_list
    def get(self, request):
        queryset = Clinic.objects.all()
        filter = ClinicFilter(request.GET, queryset=queryset)
        serializer = ClinicListSerializer(filter.qs, many=True)
        return Response(serializer.data)
    

class ClinicRetrieveView(APIView):
    @doc_clinic_retrieve
    def get(self, request, pk):
        instance = get_object_or_404(Clinic, pk=pk)
        serializer = ClinicRetrieveSerializer(instance=instance)
        return Response(serializer.data)
