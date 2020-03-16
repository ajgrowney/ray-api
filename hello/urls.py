from django.urls import path
from .views import echoView, echoTimeView

urlpatterns = [
    path('hello', echoView),
    path('time', echoTimeView)
]
