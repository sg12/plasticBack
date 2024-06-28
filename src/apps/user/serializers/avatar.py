from rest_framework import serializers
from apps.user.models import User


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar',)
