from rest_framework.response import Response


class ErrorResponse(Response):
    def __init__(self, *args, **kwargs):
        data = kwargs.get('data', None)
        if data:
            kwargs['data'] = {"detail": data}

        super().__init__(*args, **kwargs)