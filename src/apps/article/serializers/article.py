from rest_framework import serializers
from apps.article.models import Article
from .author import ArticleAuthorSerializer


class ArticleSerializer(serializers.ModelSerializer):
    author = ArticleAuthorSerializer()
    rubric = serializers.CharField(source='rubric.name')

    class Meta:
        model = Article
        exclude = ('description',)


class ArticleRetrieveSerializer(serializers.ModelSerializer):
    author = ArticleAuthorSerializer()
    rubric = serializers.CharField(source='rubric.name')

    class Meta:
        model = Article
        exclude = ('short',)
