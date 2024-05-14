from rest_framework import serializers
from apps.doctor.models import Qualification


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        exclude = ('doctor',)

   
class QualificationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        exclude = ()
        

class QualificationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        exclude = ('doctor',)
