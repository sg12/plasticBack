from rest_framework import serializers
from apps.clinic.models import Clinic
from apps.user.serializers import BaseUserFields


class BaseClinicFields(BaseUserFields):
    fio = None
    director = serializers.CharField(source='user.username')
    metro = serializers.CharField(source='metro.name', default=None)
    district = serializers.CharField(source='district.name', default=None)
    city = serializers.CharField(source='city.name', default=None)
    rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()


class ClinicSerializer(BaseClinicFields):
    class Meta:
        model = Clinic
        fields = (
            'name',
            'phone',
            'description',
            'address',
            'metro',
            'district',
            'city',
            'rating',
            'reviews_count'
        )


class ClinicRetrieveSerializer(BaseClinicFields):
    class Meta:
        model = Clinic
        exclude = ('user',)


class ClinicUpdateSerializer(BaseClinicFields):
    class Meta:
        model = Clinic
        fields = (
            'name',
            'official_name',
            'phone',
            'description',
            'site',
            'address',
            'metro',
            'district',
            'city'
        )
