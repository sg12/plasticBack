from rest_framework import serializers
from apps.clinics.models import Clinic
from apps.users.serializers import UserRetrieveSerializer
from apps.services.serializers import ServiceUpdateSerializer
from .review import ReviewReadSerializer


class ClinicListSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer()
    services = ServiceUpdateSerializer(many=True)
    metro = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()

    
    class Meta:
        model = Clinic
        fields = '__all__'
        

class ClinicReadSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer()
    metro = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()
    reviews = ReviewReadSerializer(many=True)
    
    class Meta:
        model = Clinic
        fields = '__all__'


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