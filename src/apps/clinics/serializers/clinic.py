from rest_framework import serializers
from apps.clinics.models import Clinic


class ClinicListSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.username')
    avatar = serializers.CharField(source='user.avatar')
    address = serializers.CharField(source='user.address')
    phone = serializers.CharField(source='user.phone')
    rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()

    
    class Meta:
        model = Clinic
        fields = (
            'id',
            'name',
            'avatar',
            'address',
            'phone',
            'description',
            'metro',
            'district',
            'open_time',
            'close_time',
            'rating',
            'reviews_count',
        )
        depth = 1
        

class ClinicRetrieveSerializer(ClinicListSerializer):
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Clinic
        exclude = ('user', )


class ClinicUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = (
            'id',
            'director',
            'open_time',
            'close_time',
            'description',
        )