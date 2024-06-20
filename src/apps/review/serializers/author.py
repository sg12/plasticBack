from rest_framework import serializers
from apps.user.models import User


class ReviewAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'email',
            'username',
            'avatar'
        )
