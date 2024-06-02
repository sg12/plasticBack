from rest_framework import serializers
from apps.support.models import Ticket
from .author import AuthorSerializer


class TicketSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    
    class Meta:
        model = Ticket
        exclude = ()


class TicketCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Ticket
        exclude = ()


class TicketUpdateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Ticket
        exclude = ()
