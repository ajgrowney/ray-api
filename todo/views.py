from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

# Create your views here.
def CheckCalendar(request:WSGIRequest):
    qparams = request.GET
    message = "Checking Calendar"
    return HttpResponse(message, status=200, content_type="text/plain")

def CheckToday(request:WSGIRequest):
    qparams = request.GET
    message = "Today's Events:"
    return HttpResponse(message, status=200, content_type="text/plain")

def CheckReminders(request:WSGIRequest):
    return HttpResponse("Checking Reminders", status=200, content_type="text/plain")