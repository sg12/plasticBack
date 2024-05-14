from rest_framework.filters import OrderingFilter
from rest_framework.response import Response


class PagePagination(OrderingFilter):
    page_size_query_param = 'limit'
    
    ordering_title = 'Сортировка'
    ordering_description = 'Сортировка по'
    