from rest_framework import serializers
from apps.doctor.models import Doctor
from apps.reception.models import ReceptionType
from apps.user.serializers import BaseUserFields
from .clinic import ClinicInfoSerilaizer
from pkg.serializers import UserUpdate


class DoctorSerializer(BaseUserFields):
    serializer_choice_field = serializers.ModelSerializer
    clinic = ClinicInfoSerilaizer()
    reception_types = serializers.ListSerializer(child=serializers.CharField())
    specialization = serializers.CharField(source='specialization.name', default=None)
    category = serializers.CharField(source='category.name', default=None)
    degree = serializers.CharField(source='degree.name', default=None)
    gender = serializers.CharField(source='user.gender')
    rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()
    
    class Meta:
        model = Doctor
        exclude = ('user',)


class DoctorUpdateSerializer(UserUpdate, serializers.ModelSerializer):
    fio = serializers.CharField(source='user.username')
    reception_types = serializers.SlugRelatedField(
        slug_field='name', 
        queryset=ReceptionType.objects.all(), 
        many=True
    )
    
    class Meta:
        model = Doctor
        fields = (
            'fio',
            'site',
            'address',
            'description',
            'category',
            'degree',
            'specialization',
            'experience',
            'phone',
            'reception_types',
        )
