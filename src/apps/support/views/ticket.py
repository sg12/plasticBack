from pkg.generics import (
    ListCreateAPIView,
    UpdateDestroyAPIView
)
from apps.support.models import Ticket
from apps.support.serializers import *


class TicketView(ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateSerializer
    result_class = TicketSerializer


class TicketDetailView(UpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketUpdateSerializer
    result_class = TicketSerializer
