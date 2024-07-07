from rest_framework import serializers
from apps.service.models import Service
from apps.doctor.serializers import DoctorSerializer


class DoctorServiceSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    
    class Meta:
        model = Service
        fields = (
            'id',
            'doctor',
            'price'
        )
