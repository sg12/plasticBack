from rest_framework import serializers
from apps.clinic.models import Clinic


class ClinicInfoSerilaizer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.username')
    metro = serializers.CharField(source='metro.name')
    district = serializers.CharField(source='district.name')
    city = serializers.CharField(source='city.name')
    
    class Meta:
        model = Clinic
        fields = (
            'id',
            'name',
            'official_name',
            'address',
            'metro',
            'district',
            'city',
        )
