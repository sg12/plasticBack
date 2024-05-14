from rest_framework import serializers
from apps.user.models import User


class BaseUserFields(serializers.ModelSerializer):
    id = serializers.IntegerField(source='user.id')
    email = serializers.EmailField(source='user.email')
    fio = serializers.CharField(source='user.username')
    avatar = serializers.ImageField(source='user.avatar')


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='role.name')
    
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'role',
            'avatar',
            'created_at',
            'confidentiality_consent',
            'personal_data_consent',
            'review_consent',
            'news_consent',
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'avatar',
            'confidentiality_consent',
            'personal_data_consent',
            'review_consent',
            'news_consent',
        )
