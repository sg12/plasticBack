from rest_framework.generics import RetrieveAPIView
from apps.doctor.models import Doctor
from apps.doctor.serializers import *
from apps.doctor.filters import DoctorFilter
from pkg.pagination import PagePagination
from pkg.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from apps.doctor.permissions import IsDoctor
from apps.user.models import User, Role
from django.utils.decorators import method_decorator
from pkg.decorators import is_doctor
from apps.doctor.schemas import *


@doc_doctor
class DoctorView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filterset_class = DoctorFilter
    pagination_class = PagePagination

@doc_doctor_detail
@is_doctor
class DoctorDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = DoctorSerializer

    def get_object(self):
        user = super().get_object()
        return user.doctor

class ProfileDoctorDetailView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, IsDoctor)
    serializer_class = DoctorUpdateSerializer
    result_class = DoctorSerializer

    def get_object(self):
        return self.request.user.doctor
