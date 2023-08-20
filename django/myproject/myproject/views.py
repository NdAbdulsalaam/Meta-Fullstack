from django.http import HttpResponse


def handler404(request, exception):
    return HttpResponse("Page not found")