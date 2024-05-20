from django.shortcuts import render
from django.http import HttpResponse

# Create your views here

def helloworld_view(request):
    return HttpResponse("Hello WOC7014 Teams!")



