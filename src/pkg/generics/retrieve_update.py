from .base_detail import BaseDetailAPIView
from rest_framework.mixins import RetrieveModelMixin
from pkg.mixins import UpdateModelMixin


class RetrieveUpdateAPIView(RetrieveModelMixin, UpdateModelMixin, BaseDetailAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.partial_update(request, *args, **kwargs)
