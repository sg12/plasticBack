from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.articles.models import Article
from apps.articles.serializers import ArticleReadSerializer
from rest_framework.response import Response
from apps.articles.filters import ArticleFilter
from rest_framework.pagination import LimitOffsetPagination
from apps.articles.yasg import doc_articles_list


__all__ = (
    'ArticleListView',
    'ArticleRetrieveView'
)


class ArticleListView(ListAPIView):
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleReadSerializer

    @doc_articles_list
    def get(self, request):
        queryset = self.get_queryset()
        filter = ArticleFilter(request.GET, queryset=queryset)

        paginator = LimitOffsetPagination()
        paginator.default_limit = 10
        queryset = paginator.paginate_queryset(filter.qs, request)

        serializer = ArticleReadSerializer(queryset, many=True)

        response = Response(data=serializer.data)
        response.headers['X-Total-Count'] = len(serializer.data)
        return response


class ArticleRetrieveView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleReadSerializer