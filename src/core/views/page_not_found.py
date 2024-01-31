from django.shortcuts import HttpResponse


def custom_handler_404(request, exception):
    content = '{"detail": "Страница не найдена"}'
    return HttpResponse(status=404, content=content, headers={"Content-Type": "application/json"})
