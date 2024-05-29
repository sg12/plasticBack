from apps.review.models import Review
from apps.review.serializers import *
from rest_framework.generics import ListAPIView
from pkg.generics import ListCreateAPIView, UpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from apps.review.permissions import HasReceptionOrReadOnly, IsAuthorReply
from apps.client.permissions import IsClientOrReadOnly
from pkg.permissions import IsDoctorOrClinic


class ReviewView(ListCreateAPIView):
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, IsClientOrReadOnly)
    serializer_class = ReviewCreateSerializer
    result_class = ReviewSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user_pk = self.kwargs.get('user_pk')
        return queryset.filter(user__pk=user_pk)


class ReviewDetailView(UpdateDestroyAPIView):
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, IsClientOrReadOnly)
    serializer_class = ReviewUpdateSerializer
    result_class = ReviewSerializer


class ProfileReviewView(ListAPIView):
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, IsDoctorOrClinic)
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
