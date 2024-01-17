from rest_framework import serializers
from apps.clinics.models import Service


class ClinicServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
