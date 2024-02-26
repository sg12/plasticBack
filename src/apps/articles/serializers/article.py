from rest_framework import serializers
from apps.articles.models import Article
from apps.accounts.serializers import UserRetrieveSerializer


class ArticleReadSerializer(serializers.ModelSerializer):
    author = UserRetrieveSerializer()
    class Meta:
        model = Article
        exclude = ()