from apps.review.models import Review
from apps.review.serializers import *
from rest_framework.generics import ListAPIView
from pkg.generics import ListCreateAPIView, UpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from apps.review.permissions import IsAuthorReview
from apps.client.permissions import IsClientOrReadOnly
from pkg.permissions import IsDoctorOrClinic
from apps.review.schemas import *


class BaseReviewView(ListCreateAPIView):
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, IsClientOrReadOnly)
    serializer_class = ReviewCreateSerializer
    result_class = ReviewSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user_pk = self.kwargs.get('user_pk')
        return queryset.filter(user__pk=user_pk)
    

@doc_review_doctor
class ReviewDoctorView(BaseReviewView):
    pass


@doc_review_clinic
class ReviewClinicView(BaseReviewView):
    pass


@doc_review_detail
class ReviewDetailView(UpdateDestroyAPIView):    
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, IsAuthorReview)
    serializer_class = ReviewUpdateSerializer
    result_class = ReviewSerializer


@doc_profile_review
class ProfileReviewView(ListAPIView):
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, IsDoctorOrClinic)
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
