from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.articles.models import Article
from apps.articles.serializers import ArticleReadSerializer


__all__ = (
    'ArticleListView',
    'ArticleRetrieveView'
)

class ArticleListView(ListAPIView):
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleReadSerializer


class ArticleRetrieveView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleReadSerializer