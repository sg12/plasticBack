from rest_framework.response import Response
from apps.surgeons.models import Review, Surgeon
from apps.surgeons.serializers import (
    ReviewCreateSerializer,
    ReviewUpdateSerializer
)
from rest_framework.views import APIView
from apps.surgeons.yasg import doc_review_create, doc_review_update


class SurgeonAddReviewView(APIView):
    @doc_review_create
    def post(self, request, pk):
        clinic = Surgeon.objects.filter(pk=pk).first()

        if clinic is None:
            data = {
                'detail': 'Не удалось добавить отзыв на данного врача'
            }
            return Response(status=404, data=data)

        instance = Review.objects.filter(surgeon_id=pk, user=request.user).first()

        request.data.update({'surgeon_id': pk})

        serializer = ReviewCreateSerializer(instance=instance, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=204)

    def update(self, request, pk):
        instance = Review.objects.filter(surgeon_id=pk, user=request.user).first()

        if instance is None:
            data = {
                'detail': 'Ошибка при редактировании отзыва'
            }
            return Response(status=404, data=data)

        request.data.update({'surgeon_id': pk})

        serializer = ReviewUpdateSerializer(instance=instance, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=204)

    @doc_review_update
    def put(self, request, pk):
        return self.update(request, pk)

    @doc_review_update
    def patch(self, request, pk):
        return self.update(request, pk)