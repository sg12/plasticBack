from rest_framework import serializers
from apps.clinics.models import Clinic


__all__ = [
    'ClinicSerializer',
    'ClinicCreateSerializer',
]


class ClinicSerializer(serializers.ModelSerializer):
    metro = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    services = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    
    class Meta:
        model = Clinic
        fields = (
            'name',
            'address',
            'image',
            'metro',
            'services',
            'type',
            'price',
            'phone',
            'work_time',
            'date_created',
        )
        

class ClinicCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = (
            'name',
            'address',
            'image',
            'metro',
            'services',
            'type',
            'price',
            'phone',
            'work_time',
            'date_created',
        )