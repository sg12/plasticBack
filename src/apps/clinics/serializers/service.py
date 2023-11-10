from rest_framework import serializers
from apps.clinics.models import Service


__all__ = ['ServiceSerializer']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name',)