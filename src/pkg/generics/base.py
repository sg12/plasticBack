from rest_framework.generics import GenericAPIView
from pkg.mixins import BaseModelMixin


class BaseAPIView(BaseModelMixin, GenericAPIView):
    pass
