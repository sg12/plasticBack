from rest_framework import serializers
from apps.accounts.models import Review
from .user import UserRetrieveSerializer
from .validators import rating_validator


class ReviewRetrieveSerializer(serializers.ModelSerializer):
    author = UserRetrieveSerializer(default=serializers.CurrentUserDefault(), read_only=True)
    target = UserRetrieveSerializer()

    class Meta:
        model = Review
        fields = '__all__'


class ReviewListSerializer(ReviewRetrieveSerializer):
    pass


class ReviewCreateSerializer(ReviewRetrieveSerializer):
    target_id = serializers.IntegerField(write_only=True)
    rating = serializers.IntegerField(validators=(rating_validator,))

    class Meta:
        model = Review
        fields = '__all__'


class ReviewUpdateSerializer(ReviewCreateSerializer):
    target_id = serializers.IntegerField(read_only=True)
