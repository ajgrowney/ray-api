from django.http import HttpResponse
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.

def GetRecipes(request:WSGIRequest):
    message = "Getting recipes"
    return HttpResponse(message, status=200, content_type="text/plain")

def GetGroceries(request:WSGIRequest):
    message = "Getting groceries"
    return HttpResponse(message, status=200, content_type="text/plain")