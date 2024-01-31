from rest_framework import serializers
from apps.services.models import ServiceInfo


def valid_service_info(value):
    try:
        ServiceInfo.objects.get(id=value)
    except ServiceInfo.DoesNotExist:
        raise serializers.ValidationError(f'Запись не найдена')