import os.path
import json
from django.shortcuts import render
from django.core import serializers
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.forms.models import model_to_dict
import sqlite3
from .models import Reminder as ReminderDB, Chore as ChoreDB
from datetime import datetime, timedelta
from api_base import StandardResponse

# Create your views here.
def Reminders(request:WSGIRequest):
    if request.method == 'GET':
        try:
            if 'verbose' in request.GET:
                reminders = list(ReminderDB.objects.values())
            else:
                reminders = [r.text for r in ReminderDB.objects.all()] 
            response = reminders
            responseCode = 200 if len(reminders) > 0 else 204
        except Exception as e:
            return StandardResponse(500, str(e))
    elif request.method == 'POST':
        try:
            request_body = json.loads(request.body)
        except:
            responseCode = 400
            response = ["Bad request: Malformed JSON Input"]
            return StandardResponse(responseCode, response)

        if 'text' not in request_body:
            responseCode = 400
            response = ["Bad Request: missing 'text' query parameter"]
        else:
            reminder_text = request_body['text']
            try:
                reminder_priority = int(request_body['priority'])
            except:
                reminder_priority = -1

            reminder = ReminderDB.objects.create(text=reminder_text, priority=reminder_priority, time=datetime.now()) 
            reminder.save()
            responseCode = 201
            response = [{ "id": reminder.id }]
        
    return StandardResponse(responseCode, response)

def Reminder(request:WSGIRequest, id:int):
    if request.method == 'DELETE':
        
        try:
            ReminderDB.objects.get(id=id).delete()
            return StandardResponse(204, [])
        except ReminderDB.DoesNotExist as e:
            return StandardResponse(404, ["Resource does not exist"])
        except Exception as e:
            return StandardResponse(500, [str(e)])
    
    elif request.method == 'GET':
        try:
            obj = ReminderDB.objects.get(id=id)
            response = model_to_dict(obj)
            return StandardResponse(200, [response])
        except ReminderDB.DoesNotExist as e:
            return StandardResponse(404, ["Resource does not exist"])
        except Exception as e:
            return StandardResponse(500, [str(e)])
    
    else:
        return StandardResponse(405, [])
        
def Chores(request:WSGIRequest):
    if request.method == "GET":
        chores = list(ChoreDB.objects.values())
        responseCode = 200 if len(chores) > 0 else 204
        response = chores
    elif request.method == "POST":
        responseCode, response = 500, ["Not implemented yet"]
    else:
        responseCode, response = 405, []

    return StandardResponse(responseCode, response)
