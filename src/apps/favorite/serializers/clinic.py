from rest_framework import serializers
from apps.user.models import User


class ClinicInfoSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='username')
    
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'avatar',
        )
