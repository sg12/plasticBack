from rest_framework import serializers
from apps.service.models import Specialty
from .specialty import SpecialtySerializer
from apps.service.models import Service
from django.utils.translation import gettext as _


class ServiceSerializer(serializers.ModelSerializer):
    speciality = SpecialtySerializer()

    class Meta:
        model = Service
        exclude = ('user',)


class ServiceCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    speciality = serializers.PrimaryKeyRelatedField(queryset=Specialty.objects.all())

    class Meta:
        model = Service
        exclude = ()


class ServiceUpdateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Service
        fields = (
            'user',
            'price',
            'status'
        )
