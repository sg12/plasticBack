from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.articles.models import Article
from apps.articles.serializers import ArticleReadSerializer
from rest_framework.response import Response


__all__ = (
    'ArticleListView',
    'ArticleRetrieveView'
)


class ArticleListView(ListAPIView):
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleReadSerializer

    def get(self, request):
        queryset = self.get_queryset()
        serializer = ArticleReadSerializer(queryset, many=True)
        response = Response(data=serializer.data)
        response.headers['X-Total-Count'] = len(serializer.data)
        return response


class ArticleRetrieveView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleReadSerializer