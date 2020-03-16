from django.http import HttpResponse
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.
def GenerateOutfit(request:WSGIRequest):
    print(request.method)
    qparams = request.GET
    shirt_id, pants_id = qparams.get('shirt'), qparams.get('pants')
    print(shirt_id, pants_id)
    message="Generate outfit"
    return HttpResponse(message, status=200, content_type="text/plain")