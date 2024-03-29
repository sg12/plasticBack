from rest_framework import serializers
from apps.surgeons.models import Surgeon
from apps.accounts.serializers import UserRetrieveSerializer


class SurgeonRetrieveSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer()
    clinic_name = serializers.CharField(source='clinic.user.username', read_only=True, default="")
    rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()

    class Meta:
        model = Surgeon
        exclude = ('clinic', )


class SurgeonListSerializer(SurgeonRetrieveSerializer):
    pass


class SurgeonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surgeon
        fields = (
            'clinic',
            'description',
            'category',
            'academic',
            'specialtie',
            'experience',
            'reception',
        )