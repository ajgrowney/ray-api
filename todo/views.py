import os.path
from django.shortcuts import render
from django.core import serializers
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
import sqlite3
from .models import Reminder as ReminderDB
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

def Reminders(request:WSGIRequest):
    if request.method == 'GET':
        if 'verbose' in request.GET:
            reminders = list(ReminderDB.objects.values())
        else:
            reminders = [r.text for r in ReminderDB.objects.all()] 

        if len(reminders) == 0:
            responseCode, response = 204,[] 
        else:
            responseCode, response= 200, reminders

    elif request.method == 'POST':
        new_reminder = request.GET.get('reminder', default=None)
        if not new_reminder:
            responseCode = 400
            response = ["Bad Request: missing 'reminder' query parameter"]
        else:
            new_priority = request.GET.get('priority', default=-1)
            reminder = ReminderDB.objects.create(text=new_reminder, priority=new_priority, time=datetime.now()) 
            reminder.save()
            responseCode = 204
            response=[]
        
    return JsonResponse(StandardResponse(responseCode, response))

def Reminder(request:WSGIRequest, id:int):
    if request.method == 'DELETE':
        ReminderDB.objects.get(id=id).delete()
        return JsonResponse(StandardResponse(200, [id]))
    elif request.method == 'GET':
        obj = ReminderDB.objects.get(id=id)
        obj = obj.text
        return JsonResponse(StandardResponse(200, [obj]))
    else:
        return JsonResponse(StandardResponse(405, []))