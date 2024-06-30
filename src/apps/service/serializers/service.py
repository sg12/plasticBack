from rest_framework import serializers
from apps.doctor.models import Specialization
from apps.doctor.serializers import SpecializationSerializer
from apps.service.models import Service
from django.utils.translation import gettext as _


class ServiceSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer()

    class Meta:
        model = Service
        exclude = ('user',)


class ServiceCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    specialization = serializers.PrimaryKeyRelatedField(queryset=Specialization.objects.all())

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
