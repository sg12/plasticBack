from .base import BaseAPIView
from pkg.mixins import CustomUpdateMixin
from rest_framework.mixins import RetrieveModelMixin, DestroyModelMixin
from rest_framework.response import Response


class RetrieveUpdateDestroyAPIView(RetrieveModelMixin, CustomUpdateMixin, DestroyModelMixin, BaseAPIView):
    retrieve_serializer_class = None
    update_serializer_class = None

    swagger_update = None

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.retrieve_serializer_class
        elif self.request.method in ['PUT', 'PATCH']:
            return self.update_serializer_class

        return None

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)