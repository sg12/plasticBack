from rest_framework.permissions import IsAuthenticated
from apps.client.permissions import IsClient
from pkg.generics import RetrieveUpdateAPIView
from rest_framework.generics import RetrieveAPIView
from apps.client.serializers import *
from apps.user.models import User
from pkg.decorators import is_client
from apps.client.schemas import *


@doc_client
@is_client
class ClientView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = ClientSerializer

    def get_object(self):
        user = super().get_object()
        return user.client


@doc_profile_client
class ProfileClientView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, IsClient)
    serializer_class = ClientUpdateSerializer
    result_class = ClientSerializer

    def get_object(self):
        return self.request.user.client
