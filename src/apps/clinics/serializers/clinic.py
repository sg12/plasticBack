from rest_framework import serializers
from apps.clinics.models import Clinic
from .surgeon import SurgeonSerializer
from apps.users.serializers import UserRetrieveSerializer
from pkg.serializer import UserUnpack


class ClinicListSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer()
    metro = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()
    
    class Meta:
        model = Clinic
        fields = (
            'id',
            'user',
            'metro',
            # 'work_times',
            'rating',
            'reviews_count',
        )
        depth = 1
        

class ClinicRetrieveSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer()
    surgeons = SurgeonSerializer(many=True)
    rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()
    
    class Meta:
        model = Clinic
        fields = (
            'id',
            'user',
            'metro',
            'surgeons',
            'rating',
            'reviews_count',
        )
        depth = 2