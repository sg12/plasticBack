from apps.review.models import Review
from apps.review.serializers import *
from pkg.generics import ListCreateAPIView
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated
)


class ReviewView(ListCreateAPIView):
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ReviewCreateSerializer
    result_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk', self.request.user.pk)
        return Review.objects.filter(user__pk=pk)


class ReviewDetailView(ListCreateAPIView):
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ReviewUpdateSerializer
    result_class = ReviewSerializer
