from rest_framework import serializers
from apps.license.models import License


class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        exclude = ('user',)


class LicenseCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = License
        exclude = ()
