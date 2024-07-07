from pkg.generics import (
    ListCreateAPIView,
    UpdateDestroyAPIView
)
from apps.support.models import Message
from apps.support.serializers import *
from apps.support.schemas import *
from rest_framework.permissions import IsAuthenticated
from apps.support.permissions import IsAuthorTicketOrAdmin


@doc_message
class MessageView(ListCreateAPIView):
    queryset = Message.objects.order_by('-created_at')
    permission_classes = (IsAuthenticated, IsAuthorTicketOrAdmin)
    serializer_class = MessageCreateSerializer
    result_class = MessageSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(ticket__pk=pk)


@doc_message_detail
class MessageDetailView(UpdateDestroyAPIView):
    queryset = Message.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageUpdateSerializer
    result_class = MessageSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
