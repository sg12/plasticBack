from rest_framework import serializers
from apps.clinics.models import Clinic
from .surgeon import SurgeonSerializer
from apps.users.serializers import UserRetrieveSerializer


class ClinicListSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer()
    metro = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()
    
    class Meta:
        model = Clinic
        fields = '__all__'
        depth = 1
        

class ClinicReadSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer()
    surgeons = SurgeonSerializer(many=True)
    metro = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()
    
    class Meta:
        model = Clinic
        fields = (
            'id',
            'user',
            'director',
            'open_time',
            'close_time',
            'description',
            'specialization',
            'metro',
            'surgeons',
            'rating',
            'reviews_count',
        )
        depth = 2


class ClinicUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = (
            'id',
            'director',
            'open_time',
            'close_time',
            'description',
            'specialization',
        )