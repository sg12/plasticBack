from rest_framework import serializers
from apps.doctor.models import Specialty


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        exclude = ()
