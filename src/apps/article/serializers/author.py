from rest_framework import serializers
from apps.user.models import User


class ArticleAuthorSerializer(serializers.ModelSerializer):
    fio = serializers.CharField(source='username')
    
    class Meta:
        model = User
        fields = (
            'id',
            'fio',
            'avatar'
        )
