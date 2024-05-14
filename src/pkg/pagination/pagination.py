from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    page_size_query_param = 'limit'
    
    page_query_description = 'Номер страницы'
    page_size_query_description = 'Количество результатов, возвращаемых на страницу'
    
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'result': data
        })

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'count': {
                    'type': 'integer',
                    'example': 123,
                },
                'results': schema,
            },
        }
