from rest_framework import serializers
from apps.surgeons.models import Review


def star_validator(value):
    if value < 1 or value > 5:
        raise serializers.ValidationError('value is incorrect')


class ReviewReadSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = ('surgeon_id', 'user', 'star', 'text')


class ReviewCreateSerializer(serializers.ModelSerializer):
    surgeon_id = serializers.IntegerField()
    user = serializers.IntegerField(default=serializers.CurrentUserDefault())
    star = serializers.IntegerField(validators=(star_validator, ))
    
    class Meta:
        model = Review
        fields = ('surgeon_id', 'user', 'star', 'text')


class ReviewUpdateSerializer(ReviewCreateSerializer):
    pass
    