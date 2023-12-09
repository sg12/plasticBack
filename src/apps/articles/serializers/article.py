from rest_framework import serializers
from apps.articles.models import Article


class ArticleReadSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    
    class Meta:
        model = Article
        fields = (
            'id',
            'name',
            'description',
            'image',
            'category_name',
            'date_created',
            'date_updated'
        )