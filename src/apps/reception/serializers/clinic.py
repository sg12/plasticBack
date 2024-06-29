from rest_framework import serializers
from apps.reception.models import Reception, ReceptionType
from .user import ReceptionUserSerializer


class ReceptionClinicSerializer(serializers.ModelSerializer):
    specialization_name = serializers.CharField(source='service.specialization.name')
    client = ReceptionUserSerializer(source='user')
    doctor = ReceptionUserSerializer(source='service.user')
    price = serializers.FloatField(source='service.price')
    type = serializers.SlugRelatedField(slug_field='name', queryset=ReceptionType.objects.all())
    
    class Meta:
        model = Reception
        exclude = (
            'user',
            'service'
        )
