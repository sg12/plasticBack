from rest_framework import serializers
from apps.review.models import Review
from apps.user.serializers import UserPkFromUrl
from .author import AuthorSerializer


class ReviewSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Review
        exclude = (
            'user',
            'created_at',
            'updated_at'
        )


class ReviewCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.HiddenField(default=UserPkFromUrl())
    

    class Meta:
        model = Review
        exclude = ()


class ReviewUpdateSerializer(ReviewCreateSerializer):
    pass
