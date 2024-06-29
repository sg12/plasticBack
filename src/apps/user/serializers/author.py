from apps.user.models import User
from rest_framework import serializers


class GeneralAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'avatar'
        )
