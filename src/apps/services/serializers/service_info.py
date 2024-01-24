from rest_framework import serializers
from apps.services.models import ServiceInfo


class ServiceInfoRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceInfo
        fields = '__all__'


class ServiceInfoListSerializer(ServiceInfoRetrieveSerializer):
    pass
