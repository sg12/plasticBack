from rest_framework.response import Response


class ListModelMixin:
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.result_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.result_class(queryset, many=True)
        return Response(serializer.data)
