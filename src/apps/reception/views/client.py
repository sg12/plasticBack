from pkg.generics import ListCreateAPIView, UpdateDestroyAPIView
from apps.reception.models import Reception
from apps.reception.serializers import *
from rest_framework.permissions import IsAuthenticated
from apps.client.permissions import IsClient
from apps.reception.schemas import *


@doc_profile_reception_client
class ProfileReceptionClientView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsClient)
    queryset = Reception.objects.all()
    serializer_class = ReceptionClientCreateSerializer
    result_class = ReceptionClientSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


@doc_profile_reception_client_detail
class ProfileReceptionClientDetailView(UpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsClient)
    queryset = Reception.objects.all()
    serializer_class = ReceptionClientUpdateSerializer
    result_class = ReceptionClientSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(
            user=self.request.user,
            pk=pk
        )
