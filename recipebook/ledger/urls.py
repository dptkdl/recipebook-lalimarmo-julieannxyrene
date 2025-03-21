# <appname>/urls.py
from django.urls import path
from .views import RecipeListView, RecipeDetailView

urlpatterns = [
    
    path('recipes/list/', RecipeListView.as_view(), name="recipes-list"),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name="recipe-detail")
]

app_name = "ledger"