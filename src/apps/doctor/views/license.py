from rest_framework.generics import DestroyAPIView
from pkg.generics import ListCreateAPIView
from apps.doctor.models import License
from apps.doctor.serializers import *


class LicenseView(ListCreateAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseCreateSerializer
    result_class = LicenseSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(doctor__pk=pk)


class LicenseDetailView(DestroyAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseCreateSerializer
    result_class = LicenseSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(doctor__pk=pk)
