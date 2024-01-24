from rest_framework import serializers
from apps.services.models import Service
from .service_info import ServiceInfoRetrieveSerializer


class ServiceRetrieveSerializer(serializers.ModelSerializer):
    service_info = ServiceInfoRetrieveSerializer()

    class Meta:
        model = Service
        exclude = ('user', )


class ServiceListSerializer(ServiceRetrieveSerializer):
    pass


class ServiceUpdateSerializer(serializers.ModelSerializer):
    price = serializers.FloatField(required=False)
    active = serializers.BooleanField(required=False)

    class Meta:
        model = Service
        fields = ('price', 'active')