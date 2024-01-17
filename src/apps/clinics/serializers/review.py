from rest_framework import serializers
from apps.clinics.models import Review


def star_validator(value):
    if value < 1 or value > 5:
        raise serializers.ValidationError('value is incorrect')


class ReviewCreateSerializer(serializers.ModelSerializer):
    clinic_id = serializers.IntegerField()
    author = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    star = serializers.IntegerField(validators=(star_validator, ))
    
    class Meta:
        model = Review
        fields = ('clinic_id', 'author', 'text', 'star')