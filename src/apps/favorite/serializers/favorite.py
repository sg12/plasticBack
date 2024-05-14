from rest_framework import serializers
from apps.user.models import User
from apps.user.serializers import UserSerializer
from apps.favorite.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    account = UserSerializer()
    
    class Meta:
        model = Favorite
        exclude = ()


class FavoriteCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Favorite
        exclude = ()
