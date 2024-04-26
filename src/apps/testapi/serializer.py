from rest_framework import serializers
from .models import Statiy

class StatiySerializer(serializers.ModelSerializer):

    class Meta:
        model = Statiy
        fields = '__all__'
