from rest_framework import serializers
from apps.doctor.models import Doctor


class EmployeDoctorSerializer(serializers.ModelSerializer):
    fio = serializers.CharField(source='user.username')
    avatar = serializers.ImageField(source='user.avatar')
    
    class Meta:
        model = Doctor
        fields = (
            'id',
            'fio',
            'avatar',
        )
