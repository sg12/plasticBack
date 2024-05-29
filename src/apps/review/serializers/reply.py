from rest_framework import serializers
from apps.review.models import Reply
from .author import AuthorSerializer


class CurrentReply:
    requires_context = True

    def __call__(self, serializer_field):
        kwargs = serializer_field.context['kwargs']
        return kwargs['pk']


class ReplySerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Reply
        exclude = ('review',)


class ReplyCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    review = serializers.HiddenField(default=CurrentReply())
    
    class Meta:
        model = Reply
        exclude = ()


class ReplyUpdateSerializer(ReplyCreateSerializer):
    pass
