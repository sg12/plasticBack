from apps.review.models import Review
from apps.review.serializers import *
from rest_framework.generics import ListAPIView
from pkg.generics import LCUD_APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from apps.review.permissions import IsAuthorReview, OnlyOneReview
from apps.client.permissions import IsClientOrReadOnly
from pkg.permissions import IsDoctorOrClinic
from apps.review.schemas import *
from django.shortcuts import get_object_or_404


class BaseReviewView(LCUD_APIView):
    queryset = Review.objects.order_by('-created_at')
    permission_classes = (
        IsAuthenticatedOrReadOnly, 
        IsClientOrReadOnly, 
        OnlyOneReview,
        IsAuthorReview
    )
    create_serializer = ReviewCreateSerializer
    update_serializer = ReviewUpdateSerializer
    result_class = ReviewSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        pk = self.kwargs.get('pk')
        return queryset.filter(user_id=pk)
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(
            Review, 
            user_id=pk,
            author=self.request.user
        )
    

@doc_review_doctor
class ReviewDoctorView(BaseReviewView):
    pass


@doc_review_clinic
class ReviewClinicView(BaseReviewView):
    pass


@doc_profile_review
class ProfileReviewView(ListAPIView):
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated, IsDoctorOrClinic)
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
