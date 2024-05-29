from rest_framework import serializers
from apps.doctor.models import Workplace
from apps.doctor.serializers.utils import CurrentDoctorDefault


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        exclude = ('doctor',)

   
class WorkplaceCreateSerializer(serializers.ModelSerializer):
    doctor = serializers.HiddenField(default=CurrentDoctorDefault())
    
    class Meta:
        model = Workplace
        exclude = ()
        

class WorkplaceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        exclude = ('doctor',)
