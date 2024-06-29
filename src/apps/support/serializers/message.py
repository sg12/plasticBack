from rest_framework import serializers
from apps.support.models import Message, Ticket
from .author import AuthorSerializer
from pkg.serializers import EntityFromURL


class MessageSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    
    class Meta:
        model = Message
        exclude = ('ticket',)


class MessageCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    ticket = serializers.HiddenField(default=EntityFromURL('pk', Ticket))
    
    class Meta:
        model = Message
        exclude = ()


class MessageUpdateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Message
        exclude = ()
