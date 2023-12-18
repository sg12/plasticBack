from rest_framework import serializers
from apps.surgeons.models import Surgeon
from apps.users.serializers import UserRetrieveSerializer


class SurgeonSerializer(serializers.ModelSerializer):
    user = UserRetrieveSerializer(read_only=True)
    # educations = serializers.SlugRelatedField(slug_field='place', read_only=True, many=True)
    rating = serializers.FloatField()
    reviews_count = serializers.IntegerField()
    
    class Meta:
        model = Surgeon
        fields = (
            'id',
            'user',
            'site',
            'specialtie',
            'description',
            'experience',
            'category',
            'academic',
            'reception',
            'educations',
            'workplaces',
            'services',
            'rating',
            'reviews_count'
        )
        depth = 1