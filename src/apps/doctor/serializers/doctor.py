from rest_framework import serializers
from apps.doctor.models import Doctor
from apps.user.models import User, Role
from apps.reception.models import ReceptionType
from apps.user.serializers import BaseUserFields
from .clinic import ClinicInfoSerilaizer
from pkg.serializers import UserUpdate


class DoctorSerializer(BaseUserFields):
    serializer_choice_field = serializers.ModelSerializer
    clinic = ClinicInfoSerilaizer(source='clinic_user.clinic', allow_null=True)
    reception_types = serializers.ListSerializer(child=serializers.CharField())
    specialization = serializers.CharField(source='specialization.name', allow_null=True)
    category = serializers.CharField(source='category.name', allow_null=True)
    degree = serializers.CharField(source='degree.name', allow_null=True)
    gender = serializers.CharField(source='user.gender')
    rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()
    
    class Meta:
        model = Doctor
        exclude = ('user', 'clinic_user')


class DoctorUpdateSerializer(UserUpdate, serializers.ModelSerializer):
    fio = serializers.CharField(source='user.username')
    reception_types = serializers.SlugRelatedField(
        slug_field='name', 
        queryset=ReceptionType.objects.all(), 
        many=True
    )
    clinic = serializers.PrimaryKeyRelatedField(
        source='clinic_user', 
        queryset=User.objects.filter(role__name=Role.CLINIC),
        allow_null=True,
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
            'clinic'
        )
