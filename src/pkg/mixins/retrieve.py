from rest_framework.response import Response


class RetrieveModelMixin:
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.result_class(instance)
        return Response(serializer.data)
