from rest_framework import serializers
from apps.service.models import Specialty
from .specialty import SpecialtySerializer
from apps.service.models import Service
from django.utils.translation import gettext as _
from pkg import serializers as pkg_serializers


class ServiceSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer()

    class Meta:
        model = Service
        exclude = ('doctor',)
        

class ServiceNoDoctorSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer()

    class Meta:
        model = Service
        exclude = ('doctor',)


class ServiceCreateSerializer(serializers.ModelSerializer):
    doctor = serializers.HiddenField(default=pkg_serializers.CurrentUserDefault(user_field='doctor'))
    specialty = serializers.PrimaryKeyRelatedField(queryset=Specialty.objects.all())

    class Meta:
        model = Service
        exclude = ()


class ServiceUpdateSerializer(serializers.ModelSerializer):
    doctor = serializers.HiddenField(default=pkg_serializers.CurrentUserDefault(user_field='doctor'))
    
    class Meta:
        model = Service
        fields = (
            'doctor',
            'price',
            'status'
        )
