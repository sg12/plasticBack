from rest_framework.generics import RetrieveAPIView
from apps.clients.models import Client
from apps.clients.serializers import ClientRetrieveSerializer


class ClientRetrieveView(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientRetrieveSerializer
