from rest_framework import serializers
from apps.reception.models import Reception, ReceptionType
from apps.client.serializers.utils import CurrentClientDefault
from .user import ReceptionUserSerializer

# TODO: добавить адрес к приемам

class ReceptionClientSerializer(serializers.ModelSerializer):
    clinic = ReceptionUserSerializer(source='user.doctor.clinic.user')
    doctor = ReceptionUserSerializer(source='service.user')
    address = serializers.CharField(default=None)
    type = serializers.SlugRelatedField(slug_field='name', queryset=ReceptionType.objects.all())
    
    class Meta:
        model = Reception
        exclude = (
            'user',
            'service'
        )


class ReceptionClientCreateSerializer(serializers.ModelSerializer):
    client = serializers.HiddenField(source='user', default=CurrentClientDefault())
    type = serializers.SlugRelatedField(slug_field='name', queryset=ReceptionType.objects.all())
    
    class Meta:
        model = Reception
        exclude = ('status',)


class ReceptionClientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reception
        fields = ('status', 'datetime')
