import os.path
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
import sqlite3

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
    db_path = os.path.join(BASEDIR,"ray_todo.db")

    reminders = []
    with sqlite3.connect(db_path) as db:
        curs=db.cursor()
        reminders = [r[0] for r in curs.execute("SELECT reminder FROM reminders;")]

    reminders_str = ",".join(reminders)
    message = "Reminders: {0}".format(reminders_str)
    return HttpResponse(message, status=200, content_type="text/plain")
