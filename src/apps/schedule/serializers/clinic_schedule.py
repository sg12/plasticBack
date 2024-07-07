from rest_framework import serializers
from apps.schedule.models import ClinicSchedule


class ClinicScheduleSerializer(serializers.ModelSerializer):
    weekday = serializers.CharField(source='weekday.name')
    date = serializers.DateField(format="%Y-%m-%d")
    time_start = serializers.DateField(format="%H:%M")
    time_end = serializers.DateField(format="%H:%M")
    
    class Meta:
        model = ClinicSchedule
        exclude = ('user',)


class ClinicScheduleCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = ClinicSchedule
        exclude = ()


class ClinicScheduleUpdateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = ClinicSchedule
        exclude = ('weekday',)
