from rest_framework import serializers
from apps.clinics.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        # depth = 1
