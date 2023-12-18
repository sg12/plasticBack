from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from apps.services.models import Service
from apps.clinics.models import Clinic
from apps.services.serializers import ServiceSerializer
from apps.clinics.serializers import ClinicListSerializer
from apps.services.yasg import doc_service_slug_get


class ServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceSlugView(APIView):
    @doc_service_slug_get
    def get(self, request, slug):
        queryset = Clinic.objects.filter(surgeons__services__service__slug=slug)
        serializer = ClinicListSerializer(instance=queryset, many=True)
        return Response(serializer.data)
