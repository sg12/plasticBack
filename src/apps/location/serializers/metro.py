from rest_framework import serializers
from apps.location.models import Metro


class MetroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metro
        exclude = ()
