from pkg.generics import ListCreateAPIView, UpdateDestroyAPIView
from apps.support.serializers import *
from apps.support.models import Ticket
from apps.support.schemas import *


@doc_ticket
class TicketView(ListCreateAPIView):
    queryset = Ticket.objects.order_by('-created_at')
    serializer_class = TicketCreateSerializer
    result_class = TicketSerializer


@doc_ticket_detail
class TicketDetailView(UpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketUpdateSerializer
    result_class = TicketSerializer
    url_pk = 'ticket_id'
