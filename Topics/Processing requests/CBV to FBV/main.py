from django.http import HttpResponse
from django.views import View


def helloworld_view(request):
    if request.method == "GET":
        html = "Hello, World!"
        return HttpResponse(html)