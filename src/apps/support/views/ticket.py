from pkg.generics import ListCreateAPIView, UpdateDestroyAPIView
from apps.support.serializers import *
from apps.support.models import Ticket
from apps.support.schemas import *
from rest_framework.permissions import (
    IsAuthenticated, 
    IsAuthenticatedOrReadOnly
)
from apps.support.permissions import IsAuthorTicket


@doc_ticket
class TicketView(ListCreateAPIView):
    queryset = Ticket.objects.order_by('-created_at')
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = TicketCreateSerializer
    result_class = TicketSerializer


@doc_ticket_detail
class TicketDetailView(UpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    permission_classes = (IsAuthenticated, IsAuthorTicket)
    serializer_class = TicketUpdateSerializer
    result_class = TicketSerializer
