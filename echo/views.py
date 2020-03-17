from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.viewsets import ModelViewSet
from datetime import datetime
from pytz import timezone
# Create your views here.
def echoView(requestr):
    if (datetime.now(timezone('America/Denver')).hour < 12):
        message = "Good morning"
    else:
        message = "Hello" 
    return HttpResponse(message, status=200, content_type='text/plain')

def echoTimeView(request):
    message = datetime.now().time()
    return HttpResponse(message, status=200)
