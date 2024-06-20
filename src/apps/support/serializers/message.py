from rest_framework import serializers
from apps.support.models import Message
from .author import AuthorSerializer


class MessageSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    
    class Meta:
        model = Message
        exclude = ()


class MessageCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Message
        exclude = ()


class MessageUpdateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Message
        exclude = ()
