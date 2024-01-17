from rest_framework import serializers
from apps.clinics.models import ClinicService


class ClinicServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicService
        fields = ('id', 'price')
