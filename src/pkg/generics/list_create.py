from .base import BaseAPIView
from pkg.mixins import ListModelMixin, CreateModelMixin


class ListCreateAPIView(ListModelMixin, CreateModelMixin, BaseAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
