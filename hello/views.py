from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.viewsets import ModelViewSet
import datetime
# Create your views here.
def echoView(request):
    queryset = None
    return HttpResponse('Hello', status=200, content_type='text/plain')

def echoTimeView(request):
    message = datetime.datetime.now().time()
    return HttpResponse(message, status=200)