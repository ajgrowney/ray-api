import os.path
import sqlite3
from .models import Grocery
from django.http import JsonResponse
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.
BASEDIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASEDIR,"../dbs/ray_food.db")

def StandardResponse(status, results) -> dict:
    responseType = type(results[0]) if len(results) > 0 else None
    response = {"StatusCode": status, "Type": (responseType.__name__), "Results": results }
    return response

def GetRecipes(request:WSGIRequest):
    message = "Getting recipes"
    return JsonResponse(StandardResponse(200,message))

def GetGroceries(request:WSGIRequest):
    grocery_list = [g.item for g in Grocery.objects.all()] 
    return JsonResponse(StandardResponse(200,grocery_list))
