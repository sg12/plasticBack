from apps.services.models import Service
from django.http.response import Http404


def check_account_service_access(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            pk = kwargs.get('pk', None)

            instance = Service.objects.filter(pk=pk).first()

            if instance is None:
                raise Http404
            elif request.user.type not in ['clinic', 'surgeon']:
                return Http404
            elif request.user.id != instance.user.id:
                raise Http404

        return func(request, *args, **kwargs)
    return wrapper
