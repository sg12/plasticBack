from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from apps.clinic.models import Clinic
from apps.user.models import User
from apps.clinic.serializers import *
from apps.clinic.filters import *
from pkg.pagination import PagePagination
from pkg.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from apps.clinic.permissions import IsClinic
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from apps.clinic.schemas import *
from pkg.decorators import is_clinic


@doc_clinic
class ClinicView(ListAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filterset_class = ClinicFilter
    pagination_class = PagePagination
    search_fields = ('name', 'official_name', 'user__username')
    ordering_fields = ('rating', 'reviews_count')
    

@doc_clinic_detail
@is_clinic
class ClinicDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ClinicRetrieveSerializer

    def get_object(self):
        user = super().get_object()
        return Clinic.objects.get(user=user)


@doc_profile_clinic_detail
class ProfileClinicDetailView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, IsClinic)
    serializer_class = ClinicUpdateSerializer
    result_class = ClinicRetrieveSerializer

    def get_object(self):
        user = self.request.user
        return Clinic.objects.get(user=user)
