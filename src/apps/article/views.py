from rest_framework.views import APIView
from .models import Article
from .serializer import ArticleSerializer, ArticleCreateSerializer, ArticleUpdateSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .yasg import *
from django.utils.decorators import method_decorator


@method_decorator(doc_article_list, name='get')
@method_decorator(doc_article_create, name='post')
class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer


class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleUpdateSerializer
    http_method_names = ('PATCH', 'DELETE')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleSerializer
        elif self.request.method  == 'PATCH':
            return ArticleUpdateSerializer
