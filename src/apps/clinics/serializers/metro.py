from rest_framework import serializers
from apps.clinics.models import Metro


class MetroListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metro
        fields = ('id', 'name')