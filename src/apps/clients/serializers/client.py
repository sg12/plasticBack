from rest_framework import serializers
from apps.clients.models import Client
from apps.accounts.serializers import UserRetrieveSerializer


class ClientRetrieveSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer()

    class Meta:
        model = Client
        fields = ('id', 'user', 'date_born')


class ClientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('date_born',)
