from rest_framework import serializers
from apps.support.models import Comment
from apps.user.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Comment
        exclude = ()


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Comment
        exclude = ()

class CommentUpdateSerializer(CommentCreateSerializer):
    pass
