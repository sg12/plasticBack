from rest_framework.response import Response


class ErrorResponse:
    _errors: list[str] = []
    
    def __init__(self, *args, **kwargs):
        data = kwargs.get('data', None)
        if data:
            kwargs['data'] = {
                'detail': {
                    'errors': self.get_errors()
                }
            }
        
        kwargs.setdefault('status', 400)

        return Response(*args, **kwargs)
    
    def add_error(self, text: str):
        self._errors.append(text)

    def get_errors(self):
        self._errors
