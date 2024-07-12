from rest_framework import serializers
from apps.user.models import User
from apps.favorite.models import Favorite


class FavoriteDoctorSerializer(serializers.ModelSerializer):
    fio = serializers.CharField(source='username')
    specialization = serializers.CharField(source='doctor.specialization', default=None)
    role = serializers.CharField(source='role.name')
    
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'fio',
            'avatar',
            'specialization',
            'role'
        )
        

class FavoriteClinicSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='username')
    role = serializers.CharField(source='role.name')
    
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'avatar',
            'role'
        )


class FavoriteCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Favorite
        exclude = ()
