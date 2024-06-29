from rest_framework import serializers
from apps.reception.models import ReceptionType

        
class ReceptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceptionType
        fields = ('name',)
