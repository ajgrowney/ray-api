from django.urls import path
from .views import GenerateOutfit

urlpatterns = [
    path('outfit', GenerateOutfit),
]
