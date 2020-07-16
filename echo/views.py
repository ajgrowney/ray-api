from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, permissions
from rest_framework.viewsets import ModelViewSet
from datetime import datetime
from pytz import timezone
from api_base import StandardResponse
# Create your views here.
def healthCheck(request):
    return StandardResponse(200, ["healthy"])

