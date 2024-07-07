from rest_framework import serializers
from apps.doctor.models import Qualification
from apps.doctor.serializers.utils import CurrentDoctorDefault


class QualificationSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%Y-%m-%d")
    
    class Meta:
        model = Qualification
        exclude = ('doctor',)

   
class QualificationCreateSerializer(serializers.ModelSerializer):
    doctor = serializers.HiddenField(default=CurrentDoctorDefault())
    
    class Meta:
        model = Qualification
        exclude = ()
        

class QualificationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        exclude = ('doctor',)
