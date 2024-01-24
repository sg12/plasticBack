from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from apps.services.models import Service
from apps.services.serializers import (
    ServiceRetrieveSerializer,
    ServiceUpdateSerializer,
    ServiceListSerializer,
)
from django.http.response import Http404


class AccountServiceListView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceListSerializer


class AccountServiceRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceUpdateSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ServiceRetrieveSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return ServiceUpdateSerializer

        return None

    def check_service(self, request, *args, **kwargs):
        pk = kwargs.get('pk')

        instance = Service.objects.filter(pk=pk).first()

        if instance is None:
            raise Http404
        elif request.user.id != instance.user.id:
            raise Http404

    def get(self, request, *args, **kwargs):
        self.check_service(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        self.check_service(request, *args, **kwargs)
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        self.check_service(request, *args, **kwargs)
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.check_service(request, *args, **kwargs)
        return super().delete(request, *args, **kwargs)