from rest_framework.response import Response


class CustomCreateMixin:
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer = self.result_serializer(instance)
        return Response(serializer.data, status=201)
