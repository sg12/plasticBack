from rest_framework import serializers
from apps.support.models import Ticket
from apps.user.serializers import GeneralAuthorSerializer


class TicketSerializer(serializers.ModelSerializer):
    author = GeneralAuthorSerializer()
    
    class Meta:
        model = Ticket
        exclude = ()


class TicketCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Ticket
        fields = (
            'title',
            'author',
            'text'
        )
        

class TicketUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            'title',
            'text'
        )
