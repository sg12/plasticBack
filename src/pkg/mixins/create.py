from rest_framework.response import Response


class CreateModelMixin:
    result_many = False
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context={
                'request': self.request, 
                'kwargs': self.kwargs
            }
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer = self.result_class(instance=instance, many=self.result_many)
        return Response(serializer.data, status=201)
