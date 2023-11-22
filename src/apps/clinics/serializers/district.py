from rest_framework import serializers
from apps.clinics.models import District


__all__ = ['DistrictSerializer']
        

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name')