from typing import Any
from .base import BaseAPIView as _


class BaseDetailAPIView(_):
    url_pk = None
    
    def dispatch(self, request, *args, **kwargs):
        if self.url_pk:
            kwargs.setdefault('pk', kwargs.pop(self.url_pk))
        return super().dispatch(request, *args, **kwargs)
