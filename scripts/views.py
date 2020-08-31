from django.http import HttpResponse

def helloworld(response):
    return HttpResponse('hello world')
