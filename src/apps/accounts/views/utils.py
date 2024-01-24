from apps.services.models import Service
from django.http.response import Http404


def check_service(request, pk):
    instance = Service.objects.filter(pk=pk).first()

    if instance is None:
        raise Http404
    elif request.user.type not in ['clinic', 'surgeon']:
        return Http404
    elif request.user.id != instance.user.id:
        raise Http404
