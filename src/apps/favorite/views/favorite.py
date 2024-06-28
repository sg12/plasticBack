from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.generics import DestroyAPIView
from apps.favorite.serializers import *
from apps.favorite.models import Favorite
from rest_framework.permissions import IsAuthenticated
from apps.favorite.permissions import DontDublicate
from apps.client.permissions import IsClient
from apps.user.models.role import Role
from apps.favorite.schemas import *
from rest_framework.response import Response
from apps.user.models import User
from django.shortcuts import get_object_or_404


@doc_favorite_doctor
class FavoriteDoctorView(ListAPIView):
    permission_classes = (IsAuthenticated, IsClient)
    queryset = User.objects.all()
    serializer_class = FavoriteDoctorSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user_favorites__author=self.request.user,
            role__name=Role.DOCTOR
        )


@doc_favorite_clinic
class FavoriteClinicView(ListAPIView):
    permission_classes = (IsAuthenticated, IsClient)
    queryset = User.objects.all()
    serializer_class = FavoriteClinicSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user_favorites__author=self.request.user,
            role__name=Role.CLINIC
        )
        

@doc_add_favorite
class AddFavoriteView(CreateAPIView):
    permission_classes = (IsAuthenticated, IsClient, DontDublicate)
    queryset = Favorite.objects.all()
    serializer_class = FavoriteCreateSerializer
    
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        return Response(status=201)


@doc_favorite_detail
class FavoriteDetailView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsClient)
    serializer_class = None
    
    def get_object(self):
        user_pk = super().get_object()
        return get_object_or_404(
            Favorite,
            author=self.request.user,
            user_id=user_pk
        )
