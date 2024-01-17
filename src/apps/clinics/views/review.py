from rest_framework.response import Response
from apps.clinics.models import Review, Clinic
from apps.clinics.serializers import ReviewCreateSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from apps.clinics.yasg import doc_review


class ReviewView(APIView):
    @doc_review
    def post(self, request, pk):
        get_object_or_404(Clinic, pk=pk)

        instance = Review.objects.filter(clinic_id=pk, author=request.user).first()

        request.data.update({'clinic_id': pk})

        serializer = ReviewCreateSerializer(instance=instance, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(data={'msg': 'Отзыв был успешно добавлен'})
