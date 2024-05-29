from rest_framework import serializers
from apps.reception.models import Reception
from apps.doctor.serializers import DoctorSerializer
from apps.client.serializers import ClientSerializer
from apps.service.serializers import ServiceSerializer
from apps.client.serializers.utils import CurrentClientDefault

        
class ReceptionSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    client = ClientSerializer()
    doctor = DoctorSerializer()

    class Meta:
        model = Reception
        exclude = ()

class ReceptionCreateSerializer(serializers.ModelSerializer):
    client = serializers.HiddenField(default=CurrentClientDefault())
    
    class Meta:
        model = Reception
        exclude = ()


class ReceptionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reception
        fields = ('status',)


class ReceptionClientSerializer(serializers.ModelSerializer):
    clinic_name = serializers.CharField(source='user.doctor.clinic.name')
    doctor_fio = serializers.CharField(source='user.username')
    
    class Meta:
        model = Reception
        exclude = (
            'client',
            'user',
            'service'
        )

class ReceptionDoctorSerializer(serializers.ModelSerializer):
    specialization_name = serializers.CharField(source='service.specialization.name')
    client_fio = serializers.CharField(source='client.fio')
    
    class Meta:
        model = Reception
        exclude = (
            'client',
            'user',
            'service'
        )

class ReceptionClinicSerializer(serializers.ModelSerializer):
    specialization_name = serializers.CharField(source='service.specialization.name')
    client_fio = serializers.CharField(source='client.fio')
    doctor_fio = serializers.CharField(source='doctor.fio')
    
    class Meta:
        model = Reception
        exclude = (
            'client',
            'user',
            'service'
        )
