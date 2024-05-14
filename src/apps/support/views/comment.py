from pkg.generics import (
    ListCreateAPIView,
    UpdateDestroyAPIView
)
from apps.support.models import Comment
from apps.support.serializers import *


class CommentView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    result_class = CommentSerializer


class CommentDetailView(UpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    result_class = CommentSerializer
