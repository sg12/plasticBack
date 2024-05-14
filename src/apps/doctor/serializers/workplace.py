from rest_framework import serializers
from apps.doctor.models import Workplace


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        exclude = ('doctor',)

   
class WorkplaceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        exclude = ()
        

class WorkplaceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workplace
        exclude = ('doctor',)
