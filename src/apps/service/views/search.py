from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from apps.clinic.models import Clinic
from apps.doctor.models import Doctor
from apps.service.serializers import *
from apps.clinic.serializers import ClinicSerializer
from apps.doctor.serializers import DoctorSerializer


class SearchBaseAPIView(GenericAPIView):
    def get(self, request, slug):
        queryset = self.get_queryset()
        queryset = queryset.filter(user__services__specialization__slug=slug)
        
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class SearchDoctorsByServiceView(SearchBaseAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    

class SearchClinicsByServiceView(SearchBaseAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
