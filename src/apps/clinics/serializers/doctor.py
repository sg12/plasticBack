from rest_framework import serializers
from apps.clinics.models import Doctor


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