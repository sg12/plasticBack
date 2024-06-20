from apps.review.models import Review, Reply
from apps.review.serializers import *
from pkg.generics import ListCreateAPIView, UpdateDestroyAPIView
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated
)
from apps.review.permissions import *
from apps.review.schemas import (
    doc_reply, 
    doc_profile_review
)


@doc_reply
class ReplyView(ListCreateAPIView):
    queryset = Reply.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorProfile)
    serializer_class = ReplyCreateSerializer
    result_class = ReplySerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        review_id = self.kwargs.get('pk')
        return queryset.filter(review_id=review_id)


@doc_profile_review
class ReplyDetailView(UpdateDestroyAPIView):
    queryset = Reply.objects.all()
    permission_classes = (IsAuthenticated, IsAuthorReply)
    serializer_class = ReplyUpdateSerializer
    result_class = ReplySerializer
