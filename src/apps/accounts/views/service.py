from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from apps.services.models import Service
from apps.services.serializers import (
    ServiceRetrieveSerializer,
    ServiceCreateSerializer,
    ServiceUpdateSerializer,
    ServiceListSerializer,
)
from .utils import check_account_service_access
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated


@method_decorator(check_account_service_access, name="dispatch")
class AccountServiceListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Service.objects.filter(user_id=self.request.user.id)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ServiceListSerializer
        elif self.request.method == 'POST':
            return ServiceCreateSerializer


@method_decorator(check_account_service_access, name="dispatch")
class AccountServiceRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Service.objects.filter(user_id=self.request.user.id)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ServiceRetrieveSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return ServiceUpdateSerializer
