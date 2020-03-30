from django.http import JsonResponse
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.
def StandardResponse(status, results) -> dict:
        responseType = type(results[0]) if len(results) > 0 else None
        response = {"StatusCode": status, "Type": (responseType.__name__), "Results": results }
        return response

def LaundryView(request:WSGIRequest):
    message = "Checking Laundry"
    return JsonResponse(StandardResponse(200, [message]))

def GenerateOutfit(request:WSGIRequest):
    qparams = request.GET
    type_id, top_id, bottom_id = qparams.get('type'), qparams.get('top'), qparams.get('bottom')
    print(type_id,top_id, bottom_id)
    message="Generate outfit"
    return JsonResponse(StandardResponse(200, [message]))

def OutfitAccepted(request:WSGIRequest):
    return JsonResponse(StandardResponse(200, ["Outfit Accepted"]))

    
def OutfitRejected(request:WSGIRequest):
    return JsonResponse(StandardResponse(200, ["Outfit Rejected"]))
