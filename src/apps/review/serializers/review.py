from rest_framework import serializers
from apps.review.models import Review
from apps.user.serializers import UserPkFromUrl
from apps.user.models import User
from pkg.serializers.entity import EntityFromURL
from .author import ReviewAuthorSerializer


class ReviewSerializer(serializers.ModelSerializer):
    author = ReviewAuthorSerializer()

    class Meta:
        model = Review
        exclude = (
            'user',
            'created_at',
            'updated_at'
        )


class ReviewCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.HiddenField(default=EntityFromURL(name='user_pk', model=User))
    
    class Meta:
        model = Review
        exclude = ()


class ReviewUpdateSerializer(ReviewCreateSerializer):
    pass
