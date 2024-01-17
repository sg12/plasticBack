from rest_framework import serializers
from apps.clinics.models import Review
from apps.users.serializers import UserRetrieveSerializer


def star_validator(value):
    if value < 1 or value > 5:
        raise serializers.ValidationError('value is incorrect')


class ReviewReadSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Review
        fields = ('user', 'text', 'star')


class ReviewCreateSerializer(serializers.ModelSerializer):
    clinic_id = serializers.IntegerField()
    user = serializers.IntegerField(default=serializers.CurrentUserDefault())
    star = serializers.IntegerField(validators=(star_validator, ))

    class Meta:
        model = Review
        fields = ('clinic_id', 'user', 'text', 'star')


class ReviewUpdateSerializer(ReviewCreateSerializer):
    pass
