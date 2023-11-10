from rest_framework import serializers
from apps.clinics.models import Clinic


class ClinicSerializer(serializers.ModelSerializer):
    metro = serializers.StringRelatedField(many=True)
    services = serializers.StringRelatedField(many=True)
    
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