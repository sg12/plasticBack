from rest_framework import serializers
from apps.user.models import User


class DoctorInfoSerializer(serializers.ModelSerializer):
    fio = serializers.CharField(source='username')
    specialty = serializers.CharField(source='specialty.name')
    
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'fio',
            'avatar',
            'specialty'
        )
