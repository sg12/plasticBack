from rest_framework import serializers


class UnpackAccountSerializer(serializers.Serializer):
    username = serializers.CharField()
    address = serializers.CharField()
    phone = serializers.CharField()
    gender = serializers.CharField()


class AccountUpdateSerializer(serializers.Serializer):
    user = UnpackAccountSerializer()
