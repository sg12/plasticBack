from rest_framework.generics import RetrieveUpdateAPIView


class RetrieveUpdateAPIView(RetrieveUpdateAPIView):
    retrieve_serializer = None
    update_serializer = None

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.retrieve_serializer
        elif self.request.method == 'PUT' or self.request.method == 'PATCH':
            return self.update_serializer

        return None