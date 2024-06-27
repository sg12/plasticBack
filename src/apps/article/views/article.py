from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.article.models import Article
from apps.article.serializers import *
from pkg.pagination import PagePagination
from apps.article.schemas import *
from rest_framework.filters import SearchFilter


@doc_article_list
class ArticleListView(ListAPIView):
    queryset = Article.objects.order_by('created_at')
    serializer_class = ArticleSerializer
    pagination_class = PagePagination
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'author__username')


@doc_article_retrieve
class ArticleRetrieveView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleRetrieveSerializer
