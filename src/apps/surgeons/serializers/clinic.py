from rest_framework import serializers
from apps.clinics.models import Clinic
from apps.users.serializers import UserRetrieveSerializer
        

class SurgeonClinicSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer()
    
    class Meta:
        model = Clinic
        fields = (
            'id',
            'user',
            'metro',
        )
        depth = 1