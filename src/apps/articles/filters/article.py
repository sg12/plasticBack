from django_filters import rest_framework as filters
from apps.articles.models import Article
from django.db.models import Q


class ArticleFilter(filters.FilterSet):
    search = filters.CharFilter(method='get_search')
    sort = filters.CharFilter(method='get_sort')
    
    class Meta:
        model = Article
        fields = ()
        
    def get_sort(self, queryset, name, value):
        if value == 'id':
            queryset = queryset.order_by('id')
        
        return queryset

    def get_search(self, queryset, name, value):
        criterion1 = Q(name__icontains=value)
        criterion2 = Q(author__username__icontains=value)
        return queryset.filter(criterion1 | criterion2)
