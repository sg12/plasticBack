from rest_framework import serializers
from apps.reception.models import Reception, ReceptionType
from .user import ReceptionUserSerializer


class ReceptionDoctorSerializer(serializers.ModelSerializer):
    speciality = serializers.CharField(source='service.speciality.name')
    price = serializers.FloatField(source='service.price')
    client = ReceptionUserSerializer(source='user')
    type = serializers.SlugRelatedField(slug_field='name', queryset=ReceptionType.objects.all())
    
    class Meta:
        model = Reception
        exclude = (
            'user',
            'service'
        )


class ReceptionDoctorUpdateSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name', queryset=ReceptionType.objects.all())
    
    class Meta:
        model = Reception
        fields = (
            'datetime',
            'status',
            'type'
        )
