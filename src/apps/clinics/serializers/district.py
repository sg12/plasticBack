from rest_framework import serializers
from apps.clinics.models import District
        

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('name',)