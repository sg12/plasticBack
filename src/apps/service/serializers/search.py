from rest_framework import serializers
from apps.service.models import Service
from apps.doctor.models import Doctor
from apps.clinic.serializers import ClinicSerializer
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


class DoctorServiceShortSerializer(serializers.ModelSerializer):
    fio = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    avatar = serializers.ImageField(source='user.avatar')
    
    class Meta:
        model = Doctor
        fields = (
            'id',
            'fio',
            'email',
            'avatar'
        )


class ClinicServiceSerializer(serializers.ModelSerializer):
    clinic = ClinicSerializer(source='doctor.clinic')
    doctor = DoctorServiceShortSerializer()
    
    class Meta:
        model = Service
        fields = (
            'id',
            'clinic',
            'doctor',
            'price'
        )
