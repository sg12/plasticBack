from django.shortcuts import HttpResponse

def my_handler_404(request, exception):
    content = {"detail": "Страница не найдена"}
    return HttpResponse(status=404, content=str(content), headers={"Content-Type": "application/json"})