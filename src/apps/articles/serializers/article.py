from rest_framework import serializers
from apps.articles.models import Article


class ArticleReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ()