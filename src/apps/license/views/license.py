from rest_framework.generics import ListAPIView, DestroyAPIView
from pkg.generics import ListCreateAPIView
from apps.license.models import License
from apps.license.serializers import *
from rest_framework.permissions import IsAuthenticated
from pkg.permissions import IsDoctorOrClinic
from pkg.decorators import is_doctor_or_clinic
from apps.license.schemas import *
from rest_framework.parsers import MultiPartParser


@is_doctor_or_clinic
class BaseLicenseView(ListAPIView):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user_pk = self.kwargs.get('pk')
        return queryset.filter(user__pk=user_pk)


@doc_license_doctor
class LicenseDoctorView(BaseLicenseView):
    pass


@doc_license_clinic
class LicenseClinicView(BaseLicenseView):
    pass


class BaseProfileLicenseView(ListCreateAPIView):
    queryset = License.objects.all()
    permission_classes = (IsAuthenticated, IsDoctorOrClinic)
    parser_classes = (MultiPartParser,)
    serializer_class = LicenseCreateSerializer
    result_class = LicenseSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
    

class ProfileDoctorLicenseDetailView(DestroyAPIView):
    queryset = License.objects.all()
    permission_classes = (IsAuthenticated, IsDoctorOrClinic)
    serializer_class = None
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


@doc_profile_doctor_license
class ProfileDoctorLicenseView(BaseProfileLicenseView):
    pass


@doc_profile_clinic_license
class ProfileClinicLicenseView(BaseProfileLicenseView):
    pass
    

class ProfileDoctorLicenseDetailView(DestroyAPIView):
    queryset = License.objects.all()
    permission_classes = (IsAuthenticated, IsDoctorOrClinic)
    serializer_class = None
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


@doc_profile_doctor_license_detail
class ProfileDoctorLicenseDetailView(ProfileDoctorLicenseDetailView):
    pass


@doc_profile_clinic_license_detail
class ProfileClinicLicenseDetailView(ProfileDoctorLicenseDetailView):
    pass
