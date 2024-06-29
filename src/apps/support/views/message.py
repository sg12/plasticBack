from pkg.generics import (
    ListCreateAPIView,
    UpdateDestroyAPIView
)
from apps.support.models import Message
from apps.support.serializers import *
from apps.support.schemas import *
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from apps.support.permissions import IsAuthorMessage


@doc_message
class MessageView(ListCreateAPIView):
    queryset = Message.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = MessageCreateSerializer
    result_class = MessageSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        queryset = queryset.filter(ticket__pk=pk)
        return queryset.order_by('-created_at')


@doc_message_detail
class MessageDetailView(UpdateDestroyAPIView):
    queryset = Message.objects.all()
    permission_classes = (IsAuthenticated, IsAuthorMessage)
    serializer_class = MessageUpdateSerializer
    result_class = MessageSerializer
