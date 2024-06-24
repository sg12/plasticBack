from rest_framework import serializers
from apps.user.models import User


class ArticleAuthorSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'avatar'
        )
