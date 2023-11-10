from pkg.jsend import Jsend
from django.http.response import HttpResponse
from loguru import logger


class JsendException:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_exception(self, request, exception: Exception):
        jsend = Jsend(0)
        logger.exception(exception)
        return HttpResponse(jsend.error("something gone wrong"))