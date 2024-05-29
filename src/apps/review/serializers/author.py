from rest_framework import serializers
from apps.user.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'email',
            'username',
            'avatar'
        )
