from pkg.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.services.models import Service
from apps.services.serializers import (
    ServiceRetrieveSerializer,
    ServiceCreateSerializer,
    ServiceUpdateSerializer,
    ServiceListSerializer,
)
from .utils import check_account_service_access
from django.utils.decorators import method_decorator
from apps.services.yasg import *
from rest_framework.permissions import IsAuthenticated


@method_decorator(check_account_service_access, name="dispatch")
class ServiceListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    list_serializer_class = ServiceListSerializer
    create_serializer_class = ServiceCreateSerializer

    def get_queryset(self):
        return Service.objects.filter(user_id=self.request.user.id)

    @doc_service_create
    def post(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


@method_decorator(check_account_service_access, name="dispatch")
class ServiceRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    retrieve_serializer_class = ServiceRetrieveSerializer
    update_serializer_class = ServiceUpdateSerializer

    def get_queryset(self):
        return Service.objects.filter(user_id=self.request.user.id)

    @doc_service_update
    def put(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)

    @doc_service_update
    def patch(self, request, *args, **kwargs):
        return self.patch(request, *args, **kwargs)