from rest_framework.generics import ListAPIView as _
from django_filters.rest_framework import DjangoFilterBackend


class ListAPIView(_):
    filter_backends = (DjangoFilterBackend,)
