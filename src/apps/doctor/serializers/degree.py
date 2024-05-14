from rest_framework import serializers
from apps.doctor.models import Degree


class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        exclude = ()
