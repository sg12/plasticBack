from rest_framework import serializers


def rating_validator(value):
    if value < 1 or value > 5:
        raise serializers.ValidationError('value is incorrect')