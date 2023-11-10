from rest_framework import serializers
from apps.clinics.models import Doctor


__all__ = ['DoctorSerializer']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            'user',
            'address',
            'description',
            'services',
            'license',
            'site',
        )