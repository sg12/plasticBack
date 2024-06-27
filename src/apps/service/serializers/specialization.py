from rest_framework import serializers
from apps.service.models import Specialization


class SpecializationSerializer(serializers.ModelSerializer):
    operation_type = serializers.CharField(source='operation_type.name')
    
    class Meta:
        model = Specialization
        exclude = ()
