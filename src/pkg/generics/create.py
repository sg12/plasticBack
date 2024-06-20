from .base import BaseAPIView
from pkg.mixins import CreateModelMixin


class CreateAPIView(CreateModelMixin, BaseAPIView):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
