from rest_framework import serializers
from .models import Surgeon
from apps.users.serializers import UserSerializer


__all__ = ['SurgeonSerializer']


class SurgeonSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    services = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    educations = serializers.SlugRelatedField(slug_field='place', read_only=True, many=True)
    rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()
    
    class Meta:
        model = Surgeon
        fields = (
            'user',
            'clinic',
            'description',
            'license',
            'services',
            'category',
            'academic',
            'specialtie',
            'experience',
            'reception',
            'educations',
            'rating',
            'reviews_count'
        )
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        user_fields = representation['user']
        representation.update(user_fields.items())
        
        representation.pop('user')
        
        return representation