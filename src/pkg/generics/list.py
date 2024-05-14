from rest_framework.generics import ListAPIView as _


class ListAPIView(_):
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        # response.headers['X-Total-Count'] = self.paginator
        # response.headers['Access-Control-Expose-Headers'] = 'X-Total-Count'
        return response
