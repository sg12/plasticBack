from rest_framework.generics import ListAPIView, DestroyAPIView
from pkg.generics import ListCreateAPIView
from apps.license.models import License
from apps.license.serializers import *
from rest_framework.permissions import IsAuthenticated
from apps.license.permissions import IsDoctorOrClinic
from pkg.decorators import is_doctor_or_clinic
from apps.license.schemas import *
from rest_framework.parsers import MultiPartParser


@doc_license
@is_doctor_or_clinic
class LicenseView(ListAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(user__pk=pk)


@doc_profile_license
class ProfileLicenseView(ListCreateAPIView):
    queryset = License.objects.all()
    permission_classes = (IsAuthenticated, IsDoctorOrClinic)
    serializer_class = LicenseCreateSerializer
    result_class = LicenseSerializer
    parser_classes = (MultiPartParser,)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
    

@doc_profile_license_detail
class ProfileLicenseDetailView(DestroyAPIView):
    queryset = License.objects.all()
    permission_classes = (IsAuthenticated, IsDoctorOrClinic)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
