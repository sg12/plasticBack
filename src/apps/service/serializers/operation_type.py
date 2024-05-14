from rest_framework import serializers
from apps.service.models import OperationType


class OperationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationType
        exclude = ()
