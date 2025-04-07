from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeIngredientCreateView, IngredientCreateView, RecipeImageCreateView

urlpatterns = [
    path('recipes/list/',RecipeListView.as_view(), name="recipes-list"),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name="recipe-detail"),
    path('recipe/add/', RecipeCreateView.as_view(), name="recipe-create"),
    path('recipe/add/recipeingredient/', RecipeIngredientCreateView.as_view(), name="recipeingredient-create"),
    path('recipe/add/ingredient/', IngredientCreateView.as_view(), name="ingredient-create"),
    path('recipe/<int:pk>/add_image/', RecipeImageCreateView.as_view(), name="recipeimage-create"),
]