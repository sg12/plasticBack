from rest_framework.generics import RetrieveAPIView
from apps.doctor.models import Doctor
from apps.doctor.serializers import *
from apps.doctor.filters import DoctorFilter
from pkg.pagination import PagePagination
from rest_framework.generics import ListAPIView, DestroyAPIView
from pkg.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.doctor.permissions import IsDoctor
from apps.user.models import User
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from pkg.decorators import is_doctor
from apps.doctor.schemas import *


@doc_doctor
class DoctorView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filterset_class = DoctorFilter
    pagination_class = PagePagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('user__username',)


@doc_doctor_detail
@is_doctor
class DoctorDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = DoctorSerializer

    def get_object(self):
        user = super().get_object()
        return Doctor.objects.get(user=user)


@doc_profile_doctor
class ProfileDoctorView(RetrieveUpdateAPIView):
    queryset = Doctor.objects.all()
    permission_classes = (IsAuthenticated, IsDoctor)
    serializer_class = DoctorUpdateSerializer
    result_class = DoctorSerializer

    def get_object(self):
        queryset = self.get_queryset()
        return queryset.get(user=self.request.user)


class ProfileDoctorRemoveClinicView(DestroyAPIView):
    queryset = Doctor.objects.all()
    permission_classes = (IsAuthenticated, IsDoctor)
    
    def delete(self, request):
        doctor = request.user.doctor
        doctor.clinic_user = None
        
