from django.urls import path
from .views import LaundryView, GenerateOutfit, OutfitAccepted, OutfitRejected

urlpatterns = [
    path('laundry', LaundryView),
    path('outfit/accepted',OutfitAccepted),
    path('outfit/rejected',OutfitRejected),
    path('outfit', GenerateOutfit),
]
