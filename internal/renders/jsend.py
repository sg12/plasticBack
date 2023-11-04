from rest_framework.renderers import JSONRenderer
from pkg.jsend import Jsend


class JsendRender(JSONRenderer):
    charset = 'utf-8'
    
    def render(self, data, accepted_media_type=None, renderer_context=None):
        params: dict = renderer_context['request'].query_params
        
        if params.get('format') == 'json':
            jsend = Jsend()
        else:
            jsend = Jsend(4)
            
        if 'detail' in str(data):
            response = jsend.fail(data)
        elif 'ErrorDetail' in str(data):
            response = jsend.error(data)
        else:
            response = jsend.success(data)
        
        return response