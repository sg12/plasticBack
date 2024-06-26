from django.utils.deprecation import MiddlewareMixin
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.exceptions import NotFound
from django.http import JsonResponse


class PageNotFoundMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        context = {
            'view': None,
            'request': request,
        }

        response = drf_exception_handler(exception, context)

        if response is not None:
            return JsonResponse(response.data, status=response.status_code)
        
        if isinstance(exception, NotFound):
            return JsonResponse({'detail': NotFound().detail}, status=404)

        return None
