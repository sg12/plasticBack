from rest_framework.generics import ListAPIView
from pkg.generics import ListCreateAPIView, UpdateAPIView, UpdateDestroyAPIView
from apps.support.serializers import *
from apps.support.models import Ticket
from apps.support.schemas import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser


@doc_ticket
class TicketView(ListCreateAPIView):
    queryset = Ticket.objects.order_by('-created_at')
    permission_classes = (IsAuthenticated, )
    serializer_class = TicketCreateSerializer
    result_class = TicketSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


@doc_ticket_detail
class TicketDetailView(UpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TicketUpdateSerializer
    result_class = TicketSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


@doc_ticket_admin
class TicketAdminView(ListAPIView):
    queryset = Ticket.objects.order_by('-created_at')
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = TicketSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        closed = self.request.GET.get('closed')
        
        if closed is None:
            return queryset
        elif closed == 'true':
            closed = True
        else:
            closed = False

        return queryset.filter(closed=closed)


@doc_ticket_admin_detail
class TicketAdminDetailView(UpdateAPIView):
    queryset = Ticket.objects.all()
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = TicketAdminUpdateSerializer
    result_class = TicketSerializer
