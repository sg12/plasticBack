from rest_framework import serializers
from apps.service.models import Specialization


class SpecializationSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='type.name')
    
    class Meta:
        model = Specialization
        exclude = ()
