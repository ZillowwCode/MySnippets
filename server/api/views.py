from http.client import HTTPResponse
from django.shortcuts import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("<h1>Hello, World!</h1>")