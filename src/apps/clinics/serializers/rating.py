from rest_framework import serializers
from apps.clinics.models import Rating


def star_validator(value):
    if value < 1 or value > 5 :
        raise serializers.ValidationError('value is incorrect')


class RatingSerializer(serializers.ModelSerializer):    
    clinic_id = serializers.IntegerField()
    user = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    star = serializers.IntegerField(validators=(star_validator, ))
    
    class Meta:
        model = Rating
        fields = ('clinic_id', 'user', 'star')