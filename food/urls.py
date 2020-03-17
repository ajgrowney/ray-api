from django.urls import path
from .views import GetRecipes, GetGroceries

urlpatterns = [
    path('recipes', GetRecipes),
    path('groceries', GetGroceries)
]
