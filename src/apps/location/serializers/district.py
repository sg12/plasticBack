from rest_framework import serializers
from apps.location.models import District


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        exclude = ()
