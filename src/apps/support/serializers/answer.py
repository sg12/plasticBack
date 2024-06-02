from rest_framework import serializers
from apps.support.models import Answer
from .author import AuthorSerializer


class AnswerSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    
    class Meta:
        model = Answer
        exclude = ()


class AnswerCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Answer
        exclude = ()

class AnswerUpdateSerializer(AnswerCreateSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Answer
        exclude = ()
