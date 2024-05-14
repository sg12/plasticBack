from rest_framework import serializers
from apps.service.models import Service, Specialization
from apps.user.serializers import UserSerializer
from .specialization import Specialization
from django.utils.translation import gettext as _


class ServiceSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    specialization = Specialization()

    class Meta:
        model = Service
        exclude = ()


class ServiceCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    specialization = serializers.IntegerField(write_only=True)

    class Meta:
        model = Service
        exclude = ()
    
    def validate_specialization_pk(value):
        try:
            Specialization.objects.get(pk=value)
        except Specialization.DoesNotExist:
            raise serializers.ValidationError(_('The record not found'))
        return value


class ServiceUpdateSerializer(ServiceCreateSerializer):
    pass
