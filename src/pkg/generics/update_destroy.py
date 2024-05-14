from .base import BaseAPIView
from pkg.mixins import UpdateModelMixin
from rest_framework.mixins import DestroyModelMixin


class UpdateDestroyAPIView(UpdateModelMixin, DestroyModelMixin, BaseAPIView):
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
