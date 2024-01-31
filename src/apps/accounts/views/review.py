from rest_framework.response import Response
from apps.accounts.models import Review, User
from apps.accounts.serializers import (
    ReviewRetrieveSerializer,
    ReviewListSerializer,
    ReviewCreateSerializer,
    ReviewUpdateSerializer,
)
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from apps.accounts.yasg import doc_review_create, doc_review_update
from rest_framework.permissions import IsAuthenticated


class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    permission_classes = (IsAuthenticated,)


class ReviewCreateView(APIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = (IsAuthenticated,)

    @doc_review_create
    def create(self, request, **kwargs):
        user_id = kwargs.get('user_id')

        user = User.objects.filter(pk=user_id).first()

        if user is None:
            data = {'detail': 'Аккаунт пользователя не найден'}
            return Response(status=404, data=data)

        request.data.update({'target_id': user_id})

        serializer = ReviewCreateSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        instance = serializer.save()

        serializer = ReviewRetrieveSerializer(instance)

        return Response(serializer.data, status=201)


class ReviewUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewUpdateSerializer
    http_method_names = ('put', 'patch', 'delete')

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        review_id = kwargs.get('review_id')
        user_id = kwargs.get('user_id')

        queryset = self.get_queryset()

        instance = queryset.filter(id=review_id, user=request.user).first()

        if instance is None:
            data = {'detail': 'Отзыв не найден'}
            return Response(status=404, data=data)

        request.data.update({'target_id': user_id})

        serializer = self.get_serializer_class(
            instance=instance,
            data=request.data,
            context={'request': request},
            partial=partial,
       )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=200)

    @doc_review_update
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @doc_review_update
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)