from rest_framework import serializers
from rest_framework.fields import empty
from apps.surgeons.models import Rating


def star_validator(value):
    if value < 1 or value > 5 :
        raise serializers.ValidationError('value is incorrect')

class Test:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user


class RatingSerializer(serializers.ModelSerializer):
    surgeon_id = serializers.IntegerField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    star = serializers.IntegerField(validators=(star_validator, ))
    
    class Meta:
        model = Rating
        fields = ('surgeon_id', 'user', 'star')
        
    