from rest_framework import serializers
from apps.clinic.models import Clinic


class ClinicInfoSerilaizer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user.id')
    name = serializers.CharField(source='user.username')
    metro = serializers.CharField(source='metro.name', default=None)
    district = serializers.CharField(source='district.name', default=None)
    city = serializers.CharField(source='city.name', default=None)
    
    class Meta:
        model = Clinic
        fields = (
            'id',
            'name',
            'official_name',
            'address',
            'director',
            'metro',
            'district',
            'city',
        )
