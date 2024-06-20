from rest_framework.generics import RetrieveAPIView
from pkg.generics import ListAPIView
from apps.article.models import Article
from apps.article.serializers import ArticleSerializer
from pkg.pagination import PagePagination
from apps.article.schemas import *
from rest_framework.filters import SearchFilter, OrderingFilter


@doc_article_list
class ArticleListView(ListAPIView):
    queryset = Article.objects.order_by('created_at')
    serializer_class = ArticleSerializer
    pagination_class = PagePagination
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'author_name')


@doc_article_retrieve
class ArticleRetrieveView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
