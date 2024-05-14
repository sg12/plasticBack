from rest_framework import serializers
from apps.schedule.models import ClinicSchedule


class ClinicScheduleSerializer(serializers.ModelSerializer):
    weekday = serializers.CharField(source='weekday.name')
    
    class Meta:
        model = ClinicSchedule
        exclude = ()


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
