from django.http import HttpResponse
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.

def LaundryView(request:WSGIRequest):
    message = "Checking Laundry"
    return HttpResponse(message, status=200, content_type="text/plain")

def GenerateOutfit(request:WSGIRequest):
    qparams = request.GET
    shirt_id, pants_id = qparams.get('shirt'), qparams.get('pants')
    print(shirt_id, pants_id)
    message="Generate outfit"
    return HttpResponse(message, status=200, content_type="text/plain")

def OutfitAccepted(request:WSGIRequest):
    return HttpResponse("Outfit Accepted", status=200, content_type="text/plain")

    
def OutfitRejected(request:WSGIRequest):
    return HttpResponse("Outfit Rejected", status=200, content_type="text/plain")