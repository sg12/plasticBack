from rest_framework import serializers
from apps.client.models import Client
from apps.user.serializers import BaseUserFields


class BaseClientFields(BaseUserFields):
    gender = serializers.CharField(source='gender.name')
    qrcode = serializers.CharField(source='qrcode.image')


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
