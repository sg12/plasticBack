from rest_framework.generics import GenericAPIView


class BaseAPIView(GenericAPIView):
    result_serializer = None
