# <appname>/urls.py
from django.urls import path
from . import views

urlpatterns = [
    
    path('recipes/list/', views.recipe_list, name="recipes-list"),
    path('recipe/<int:id>/', views.recipe_detail, name="recipe-detail")
]

# This might be needed, Depending on your Django version
app_name = "ledger"