from rest_framework import serializers
from apps.review.models import Review
from apps.user.serializers import UserPkFromUrl
from apps.user.models import User
from pkg.serializers.entity import EntityFromURL
from .author import ReviewAuthorSerializer
from .reply import ReplySerializer


class ReviewSerializer(serializers.ModelSerializer):
    author = ReviewAuthorSerializer()
    reply = ReplySerializer()

    class Meta:
        model = Review
        fields = (
            'id',
            'author',
            'text',
            'rating',
            'created_at',
            'updated_at',
            'reply'
        )


class ReviewCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.HiddenField(default=EntityFromURL(name='pk', model=User))
    
    class Meta:
        model = Review
        exclude = ()


class ReviewUpdateSerializer(ReviewCreateSerializer):
    pass
