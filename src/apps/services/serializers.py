from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name')