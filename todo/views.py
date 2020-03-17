import os.path
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
import sqlite3
from datetime import datetime

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
    BASEDIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASEDIR,"../dbs/ray_todo.db")
    if request.method == 'GET':
        reminders = []
        with sqlite3.connect(db_path) as db:
            curs=db.cursor()
            reminders = [r[0] for r in curs.execute("SELECT reminder FROM reminders;")]

        reminders_str = ",".join(reminders)
        message = "Reminders: {0}".format(reminders_str)

    elif request.method == 'POST':
        with sqlite3.connect(db_path) as db:
            curs=db.cursor()
            print(request.GET)
            print(request.POST)
            new_reminder = request.GET['reminder']  
            sql = ''' INSERT INTO reminders(reminder,priority,time_created) VALUES(?,?,?); '''
            datarow = (new_reminder, 2,datetime.now()) 
            curs.execute(sql, datarow)
            message = "New reminder added"
        
    return HttpResponse(message, status=200, content_type="text/plain")
