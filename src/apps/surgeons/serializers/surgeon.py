from rest_framework import serializers
from apps.surgeons.models import Surgeon
from apps.users.serializers import UserRetrieveSerializer
from .clinic import SurgeonClinicSerializer


class SurgeonListSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer()
    clinic = SurgeonClinicSerializer()
    rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()
    
    class Meta:
        model = Surgeon
        exclude = ()
        

class SurgeonRetrieveSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer()
    clinic = SurgeonClinicSerializer()
    rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()
    
    class Meta:
        model = Surgeon
        exclude = ()
        depth = 1
    

class SurgeonUpdateSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Surgeon
        fields = (
            'clinic',
            'description',
            'category',
            'academic',
            'specialtie',
            'experience',
            'reception',
        )