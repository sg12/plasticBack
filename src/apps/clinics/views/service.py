from apps.clinics.models import Clinic
from rest_framework.response import Response
from django.http.response import Http404
from apps.services.serializers import ServiceListSerializer
from rest_framework.generics import ListAPIView


class ClinicServiceListView(ListAPIView):
    serializer_class = ServiceListSerializer

    def get_queryset(self):
        return Clinic.objects.filter(pk=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        clinic = self.get_object()

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(clinic.user.services, many=True)

        return Response(serializer.data)