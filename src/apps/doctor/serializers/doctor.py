from rest_framework import serializers
from apps.doctor.models import Doctor
from apps.user.serializers import BaseUserFields
from .clinic import ClinicInfoSerilaizer


class DoctorSerializer(BaseUserFields):
    clinic = ClinicInfoSerilaizer()
    reception_types = serializers.ListSerializer(child=serializers.CharField())
    specialty = serializers.CharField(source='specialty.name', default=None)
    category = serializers.CharField(source='category.name', default=None)
    degree = serializers.CharField(source='degree.name', default=None)
    gender = serializers.CharField(source='user.gender')
    rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()
    
    class Meta:
        model = Doctor
        exclude = ('user',)


class DoctorUpdateSerializer(BaseUserFields):
    class Meta:
        model = Doctor
        fields = (
            'fio',
            'site',
            'address',
            'description',
            'category',
            'degree',
            'specialty',
            'experience',
            'phone',
            'reception_types',
        )
