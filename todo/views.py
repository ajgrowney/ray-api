import os.path
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
import sqlite3
from .models import Reminder
from datetime import datetime

def StandardResponse(status, results) -> dict:
    responseType = type(results[0]) if len(results) > 0 else None
    if(responseType):
    	response = {"StatusCode": status, "Type": (responseType.__name__), "Results": results }
    else:
        response = {"StatusCode": status, "Type": "None", "Results": []}
    return response
     
# Create your views here.
def CheckCalendar(request:WSGIRequest):
    qparams = request.GET
    begin_range,end_range= qparams.get('begin'), qparams.get('end')
    print(begin_range, end_range)
    message = "Checking calendar from {0} to {1}".format(begin_range,end_range)
    return JsonResponse(StandardResponse(200, [message]))

def CheckToday(request:WSGIRequest):
    qparams = request.GET
    message = "Today's Events:"
    return JsonResponse(StandardResponse(200, [message]))

def CheckReminders(request:WSGIRequest):
    if request.method == 'GET':
        reminders = [r.text for r in Reminder.objects.all()] 
        if len(reminders) == 0:
            responseCode, response = 204,[] 
        else:
            responseCode, response= 200, reminders

    elif request.method == 'POST':
        print(request.GET)
        new_reminder = request.GET['reminder']  
        new_priority = request.GET['priority'] if 'priority' in request.GET else -1
        reminder = Reminder.objects.create(text=new_reminder, priority=new_priority,time=datetime.now()) 
        reminder.save()
        responseCode = 204
        response=[] 
        
    return JsonResponse(StandardResponse(responseCode, response))
