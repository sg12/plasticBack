from rest_framework import serializers
from apps.client.models import Client
from apps.user.serializers import BaseUserFields


class BaseClientFields(BaseUserFields):
    gender = serializers.CharField(source='user.gender')
    qrcode = serializers.CharField(source='qrcode.image', default=None)


class ClientSerializer(BaseClientFields):
    class Meta:
        model = Client
        exclude = ('user',)


class ClientUpdateSerializer(BaseUserFields):
    gender = serializers.CharField(source='user.gender')
    
    class Meta:
        model = Client
        fields = (
            'fio', 
            'phone',
            'gender', 
            'date_born'
        )
