from pkg.generics import (
    ListCreateAPIView,
    UpdateDestroyAPIView
)
from apps.support.models import Message
from apps.support.serializers import *
from apps.support.schemas import *


@doc_message
class MessageView(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageCreateSerializer
    result_class = MessageSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        ticket_id = self.kwargs.get('ticket_id')
        queryset = queryset.filter(ticket_id=ticket_id)
        return queryset.order_by('-created_at')


@doc_message_detail
class MessageDetailView(UpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageUpdateSerializer
    result_class = MessageSerializer
    url_pk = 'msg_id'
