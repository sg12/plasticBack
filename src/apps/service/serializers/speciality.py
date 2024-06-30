from rest_framework import serializers
from apps.service.models import Specialty


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        exclude = ()
