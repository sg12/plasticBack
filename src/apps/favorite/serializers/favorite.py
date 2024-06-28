from rest_framework import serializers
from apps.user.models import User
from apps.favorite.models import Favorite


class FavoriteDoctorSerializer(serializers.ModelSerializer):
    fio = serializers.CharField(source='username')
    specialty = serializers.CharField(source='specialty.name', default=None)
    
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'fio',
            'avatar',
            'specialty'
        )
        

class FavoriteClinicSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='username')
    
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'avatar',
        )


class FavoriteCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Favorite
        exclude = ()
