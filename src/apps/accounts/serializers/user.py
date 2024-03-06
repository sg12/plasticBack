from rest_framework import serializers
from apps.accounts.models import User


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'type',
            'gender',
            'avatar',
            'address',
            'phone',
            'date_created',
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'gender',
            'address',
            'phone',
        )
