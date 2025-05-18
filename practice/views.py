from django.http import HttpResponse



def http_response(request):
    return HttpResponse('<h1>This is my first django post')