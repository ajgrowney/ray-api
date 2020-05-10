from django.urls import path
from .views import ClothingItemBatchView, ClothingItemView, LaundryView, OutfitAccepted, OutfitRejected

urlpatterns = [
    path('laundry', LaundryView),
    path('outfit/accepted',OutfitAccepted),
    path('outfit/rejected',OutfitRejected),
    path('items', ClothingItemBatchView),
    path('item',ClothingItemView)
]
