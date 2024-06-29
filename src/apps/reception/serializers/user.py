from rest_framework import serializers
from apps.user.models import User


class ReceptionUserSerializer(serializers.ModelSerializer):
    fio = serializers.CharField(source='username')
    
    class Meta:
        model = User
        fields = (
            'id',
            'fio',
            'avatar'
        )
