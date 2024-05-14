from rest_framework import serializers
from apps.support.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ()


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ()


class TicketUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ()
