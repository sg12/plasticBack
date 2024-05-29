from rest_framework import serializers
from apps.support.models import Answer
from apps.user.serializers import UserSerializer


class AnswerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Answer
        exclude = ()


class AnswerCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Answer
        exclude = ()

class AnswerUpdateSerializer(AnswerCreateSerializer):
    pass
