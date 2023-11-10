from rest_framework import serializers
from apps.clinics.models import Metro


class MetroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metro
        fields = ('name',)