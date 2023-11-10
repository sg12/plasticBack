from rest_framework import serializers
from apps.clinics.models import Metro


__all__ = ['MetroSerializer']


class MetroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metro
        fields = ('name',)