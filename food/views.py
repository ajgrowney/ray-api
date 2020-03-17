import os.path
import sqlite3
from django.http import HttpResponse
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.
BASEDIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASEDIR,"../dbs/ray_food.db")
def GetRecipes(request:WSGIRequest):
    message = "Getting recipes"
    return HttpResponse(message, status=200, content_type="text/plain")

def GetGroceries(request:WSGIRequest):
    message = "Getting groceries"
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        grocery_list = [g[0] for g in cursor.execute("SELECT item FROM groceries;")]
        message = ",".join(grocery_list) 
    return HttpResponse(message, status=200, content_type="text/plain")
