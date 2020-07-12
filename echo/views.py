from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, permissions
from rest_framework.viewsets import ModelViewSet
from datetime import datetime
from pytz import timezone
# Create your views here.
def StandardResponse(status, results) -> dict:
        responseType = type(results[0]) if len(results) > 0 else None
        response = {"StatusCode": status, "Type": (responseType.__name__), "Results": results }
        return response

def healthCheck(request):
    response = StandardResponse(200, ["healthy"]) 
    print((response))
    return JsonResponse(dict(response), safe=False)

