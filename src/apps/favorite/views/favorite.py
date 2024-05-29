from pkg.generics import ListCreateAPIView
from rest_framework.generics import DestroyAPIView
from apps.favorite.serializers import *
from apps.favorite.serializers import FavoriteSerializer
from apps.favorite.models import Favorite
from rest_framework.permissions import IsAuthenticated


class FavoriteView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Favorite.objects.all()
    serializer_class = FavoriteCreateSerializer
    result_class = FavoriteSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)


class FavoriteDetailView(DestroyAPIView):
    queryset = Favorite.objects.all()
