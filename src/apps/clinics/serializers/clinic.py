from rest_framework import serializers
from apps.clinics.models import Clinic
from apps.accounts.serializers import UserRetrieveSerializer


class ClinicRetrieveSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer()
    rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()

    class Meta:
        model = Clinic
        fields = '__all__'
        depth = 1


class ClinicListSerializer(ClinicRetrieveSerializer):
    pass


class ClinicUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.RelatedField(read_only=True)

    class Meta:
        model = Clinic
        fields = '__all__'
