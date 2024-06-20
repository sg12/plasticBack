from rest_framework import serializers
from apps.user.models import User
from apps.favorite.models import Favorite
from .doctor import DoctorInfoSerializer
from .clinic import ClinicInfoSerializer


class FavoriteDoctorSerializer(serializers.ModelSerializer):
    user = DoctorInfoSerializer()
    
    class Meta:
        model = Favorite
        fields = ('user',)
        

class FavoriteClinicSerializer(serializers.ModelSerializer):
    clinic = ClinicInfoSerializer(source='user')
    
    class Meta:
        model = Favorite
        fields = ('clinic',)


class FavoriteCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Favorite
        exclude = ()
