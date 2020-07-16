from django.http import JsonResponse
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .models import ClothingItem, ClothingItemCategory
from api_base import StandardResponse
import json

# Create your views here.
def LaundryView(request:WSGIRequest):
    message = "Checking Laundry"
    return StandardResponse(200, [message])

def ClothingItemBatchView(request:WSGIRequest):
    if request.method == "GET":
        items = []
        # Get Query Parameters
        # itemCategories = request.GET.get('category', default='')
        # onlyClean = request.GET.get('clean')
        # for category in itemCategories:
        #     if onlyClean and (onlyClean.lower() == "true"):
        #         [items.append(i) for i in ClothingItem.objects.filter(category=category, remaining_tolerance__gt=0)]
        #     else:
        #         [items.append(i) for i in ClothingItem.objects.filter(category=category)]
        
        # Form Response
        if(len(items) == 0):
            responseCode, response = 204, []
        else:
            responseCode, response = 200, items
        
        return StandardResponse(responseCode, response)
    else:
        responseCode, response = 400, "Supported methods: GET"
        return StandardResponse(responseCode,response)

def ClothingItemView(request:WSGIRequest):
    if request.method == "GET":
        itemId = request.GET.get('id')
        itemSelected = ClothingItem.objects.get(id=itemId) 
        return StandardResponse(200, [itemSelected])
    elif request.method == "POST":
        response_body = json.loads(request.body)
        return StandardResponse(200, ["Item created"])
    else:
        responseCode, response = 400, "Supported methods: GET"
        return StandardResponse(responseCode,response)


def OutfitAccepted(request:WSGIRequest):
    return StandardResponse(200, ["Outfit Accepted"])

    
def OutfitRejected(request:WSGIRequest):
    return StandardResponse(200, ["Outfit Rejected"])
