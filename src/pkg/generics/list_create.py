from .base import BaseAPIView
from pkg.mixins import CustomCreateMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


class ListCreateAPIView(ListModelMixin, CustomCreateMixin, BaseAPIView):
    list_serializer_class = None
    create_serializer_class = None

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.list_serializer_class
        elif self.request.method == 'POST':
            return self.create_serializer_class

        return None