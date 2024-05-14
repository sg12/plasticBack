from rest_framework import serializers
from apps.doctor.models import Education


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ('doctor',)

   
class EducationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ()
        

class EducationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ('doctor',)
