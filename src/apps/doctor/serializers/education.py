from rest_framework import serializers
from apps.doctor.models import Education
from apps.doctor.serializers.utils import CurrentDoctorDefault


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ('doctor',)

   
class EducationCreateSerializer(serializers.ModelSerializer):
    doctor = serializers.HiddenField(default=CurrentDoctorDefault())
    
    class Meta:
        model = Education
        exclude = ()
        

class EducationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ('doctor',)
