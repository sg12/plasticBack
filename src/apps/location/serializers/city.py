from rest_framework import serializers
from apps.location.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        exclude = ()
