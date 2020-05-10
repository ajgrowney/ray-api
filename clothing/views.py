from django.http import JsonResponse
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from .models import ClothingItem, ClothingItemCategory
import json

# Create your views here.
def StandardResponse(status, results) -> dict:
    responseType = type(results[0]) if len(results) > 0 else None
    if(responseType):
        results = [result.json() for result in results]
        response = {"StatusCode": status, "Type": (responseType.__name__), "Results": results }
    else:
        response = {"StatusCode": status, "Type": "None", "Results": []}
    return response

def LaundryView(request:WSGIRequest):
    message = "Checking Laundry"
    return JsonResponse(StandardResponse(200, [message]))

def ClothingItemBatchView(request:WSGIRequest):
    if request.method == "GET":
        items = []
        # Get Query Parameters
        itemCategories = request.GET.get('category').split(',')
        onlyClean = request.GET.get('clean')
        for category in itemCategories:
            if onlyClean and (onlyClean.lower() == "true"):
                [items.append(i) for i in ClothingItem.objects.filter(category=category, remaining_tolerance__gt=0)]
            else:
                [items.append(i) for i in ClothingItem.objects.filter(category=category)]
        
        # Form Response
        if(len(items) == 0):
            responseCode, response = 204, []
        else:
            responseCode, response = 200, items
        
        return JsonResponse(StandardResponse(responseCode, response))
    else:
        responseCode, response = 400, "Supported methods: GET"
        return JsonResponse(StandardResponse(responseCode,response))

def ClothingItemView(request:WSGIRequest):
    if request.method == "GET":
        itemId = request.GET.get('id')
        itemSelected = ClothingItem.objects.get(id=itemId) 
        return JsonResponse(StandardResponse(200, [itemSelected]))
    elif request.method == "POST":
        print(json.loads(request.body.decode('utf-8')))
        return JsonResponse(StandardResponse(200, ["Item created"]))
    else:
        responseCode, response = 400, "Supported methods: GET"
        return JsonResponse(StandardResponse(responseCode,response))


def OutfitAccepted(request:WSGIRequest):
    return JsonResponse(StandardResponse(200, ["Outfit Accepted"]))

    
def OutfitRejected(request:WSGIRequest):
    return JsonResponse(StandardResponse(200, ["Outfit Rejected"]))
