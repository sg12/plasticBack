from rest_framework import serializers
from apps.clinics.models import Surgeon
from apps.users.serializers import UserSerializer


__all__ = ['SurgeonSerializer']


class SurgeonSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    clinic = serializers.SlugRelatedField(slug_field='name', read_only=True)
    services = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    
    class Meta:
        model = Surgeon
        fields = (
            'user',
            'clinic',
            'address',
            'description',
            'services',
            'license',
            'site',
        )
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        user_fields = representation['user']
        representation.update(user_fields.items())
        
        representation.pop('user')
        
        return representation