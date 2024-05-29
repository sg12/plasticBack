from apps.review.models import Review, Reply
from apps.review.serializers import *
from pkg.generics import ListCreateAPIView, UpdateDestroyAPIView
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated
)
from apps.review.permissions import *


class ReplyView(ListCreateAPIView):
    queryset = Reply.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorProfile)
    serializer_class = ReplyCreateSerializer
    result_class = ReplySerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        review_id = self.kwargs.get('review_id')
        return queryset.filter(review_id=review_id)


class ReplyDetailView(UpdateDestroyAPIView):
    queryset = Reply.objects.all()
    permission_classes = (IsAuthenticated, IsAuthorReply)
    serializer_class = ReplyUpdateSerializer
    result_class = ReplySerializer
