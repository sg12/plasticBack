from rest_framework import serializers
from apps.review.models import Review
from apps.user.models import User
from apps.user.serializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    user = UserSerializer()

    class Meta:
        model = Review
        exclude = ()


class ReviewCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Review
        exclude = ()


class ReviewUpdateSerializer(ReviewCreateSerializer):
    pass
