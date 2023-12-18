from rest_framework import serializers
from apps.clinics.models import District
        

class DistrictListSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name')