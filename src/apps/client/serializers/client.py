from rest_framework import serializers
from apps.client.models import Client
from apps.user.serializers import BaseUserFields


class BaseClientFields(BaseUserFields):
    fio = serializers.CharField(source='user.username')


class ClientSerializer(BaseClientFields):
    confidentiality_consent = serializers.BooleanField(source='user.confidentiality_consent')
    personal_data_consent = serializers.BooleanField(source='user.personal_data_consent')
    review_consent = serializers.BooleanField(source='user.review_consent')
    news_consent = serializers.BooleanField(source='user.news_consent')
    
    class Meta:
        model = Client
        exclude = ('user',)


class ClientUpdateSerializer(ClientSerializer):
    class Meta:
        model = Client
        fields = (
            'fio', 
            'avatar',
            'phone',
            'gender', 
            'date_born',
            'confidentiality_consent',
            'personal_data_consent',
            'review_consent',
            'news_consent'
        )
