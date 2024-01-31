from rest_framework.response import Response
from apps.accounts.models import Review, User
from apps.accounts.serializers import (
    ReviewRetrieveSerializer,
    ReviewListSerializer,
    ReviewCreateSerializer,
    ReviewUpdateSerializer,
)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from apps.accounts.yasg import doc_review_create, doc_review_update
from rest_framework.permissions import IsAuthenticated


class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    permission_classes = (IsAuthenticated,)

    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return ReviewListSerializer
    #     elif self.request.method == 'POST':
    #         return ReviewCreateSerializer
    #
    #     return None

    # @doc_review_create
    # def create(self, request, pk):
    #     clinic = User.objects.filter(pk=pk).first()
    #
    #     if clinic is None:
    #         data = {'detail': 'Аккаунт пользователя не найденs'}
    #         return Response(status=404, data=data)
    #
    #     instance = Review.objects.filter(author_id=pk, user=request.user).first()
    #
    #     request.data.update({'target_id': pk})
    #
    #     serializer = ReviewCreateSerializer(instance=instance, data=request.data, context={'request': request})
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     instance = serializer.save()
    #
    #     serializer = ReviewRetrieveSerializer(instance)
    #
    #     return Response(serializer.data, status=201)


class ReviewRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewRetrieveSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return ReviewUpdateSerializer

        return None

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        target_id = kwargs.get('id')

        queryset = self.get_queryset()

        instance = queryset.filter(id=kwargs.get('review_id'), user=request.user).first()

        if instance is None:
            data = {'detail': 'Отзыв не найден'}
            return Response(status=404, data=data)

        request.data.update({'target_id': target_id})

        serializer = self.get_serializer_class(
            instance=instance,
            data=request.data,
            context={'request': request},
            partial=partial,
       )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=200)