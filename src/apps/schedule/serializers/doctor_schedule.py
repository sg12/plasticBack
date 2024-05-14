from rest_framework import serializers
from apps.schedule.models import DoctorSchedule


class DoctorScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorSchedule
        exclude = ()


class DoctorScheduleCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = DoctorSchedule
        exclude = ()


class DoctorScheduleUpdateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = DoctorSchedule
        exclude = ('date',)
