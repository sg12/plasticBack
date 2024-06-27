from rest_framework import serializers
from apps.service.models import Service, Specialization
from .specialization import SpecializationSerializer
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


class ServiceUpdateSerializer(ServiceCreateSerializer):
    pass
