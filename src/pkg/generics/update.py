from .base_detail import BaseDetailAPIView
from pkg.mixins import UpdateModelMixin


class UpdateAPIView(UpdateModelMixin, BaseDetailAPIView):
    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.partial_update(request, *args, **kwargs)
