from rest_framework import serializers
from apps.services.models import Service
from .service_info import ServiceInfoRetrieveSerializer
from .validators import *


class ServiceRetrieveSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    service_info = ServiceInfoRetrieveSerializer()

    class Meta:
        model = Service
        fields = '__all__'


class ServiceListSerializer(ServiceRetrieveSerializer):
    pass


class ServiceCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    service_info_id = serializers.IntegerField(write_only=True, validators=(valid_service_info,))

    class Meta:
        model = Service
        fields = ('user', 'service_info_id', 'price', 'status')


class ServiceUpdateSerializer(ServiceCreateSerializer):
    pass