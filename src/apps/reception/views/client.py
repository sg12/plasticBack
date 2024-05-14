from pkg.generics import ListCreateAPIView, UpdateDestroyAPIView
from apps.reception.models import Reception
from apps.reception.serializers import *
from rest_framework.permissions import IsAuthenticated
from apps.client.permissions import IsClient


class ReceptionClientView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsClient)
    queryset = Reception.objects.all()
    serializer_class = ReceptionCreateSerializer
    result_class = ReceptionClientSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(client=self.request.user.client)


class ReceptionClientDetailView(UpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsClient)
    queryset = Reception.objects.all()
    serializer_class = ReceptionUpdateSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(
            client=self.request.user.client,
            pk=pk
        )
