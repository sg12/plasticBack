from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from apps.services.models import Service
from apps.services.serializers import (
    ServiceRetrieveSerializer,
    ServiceUpdateSerializer,
    ServiceListSerializer,
)
from . import utils


class AccountServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceListSerializer

    def get(self, request, *args, **kwargs):
        utils.check_service(request, kwargs.get('pk'))
        return super().get(request, *args, **kwargs)


class AccountServiceRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceUpdateSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ServiceRetrieveSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return ServiceUpdateSerializer

        return None

    def get(self, request, *args, **kwargs):
        utils.check_service(request, kwargs.get('pk'))
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        utils.check_service(request, kwargs.get('pk'))
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        utils.check_service(request, kwargs.get('pk'))
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        utils.check_service(request, kwargs.get('pk'))
        return super().delete(request, *args, **kwargs)