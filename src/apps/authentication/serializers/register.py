from rest_framework import serializers
from apps.accounts.models import User


class RegisterSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField()

    class Meta:
        model = User
        fields = ('email', 'password', 're_password')