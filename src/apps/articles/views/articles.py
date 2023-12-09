from pkg.views.read import ReadAPIView
from apps.articles.models import Article
from apps.articles.serializers import ArticleReadSerializer


class ArticleReadView(ReadAPIView):
    queryset = Article.objects.all().order_by('-pk')
    serializer_class = ArticleReadSerializer