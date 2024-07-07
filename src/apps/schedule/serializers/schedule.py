from rest_framework import serializers
from apps.schedule.models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    time = serializers.DateField(format="%H:%M")
    
    class Meta:
        model = Schedule
        exclude = ()


class ScheduleCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Schedule
        exclude = ()


class ScheduleUpdateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Schedule
        exclude = ('date',)
