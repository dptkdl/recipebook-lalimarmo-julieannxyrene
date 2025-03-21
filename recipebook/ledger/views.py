from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe

class RecipeListView(LoginRequiredMixin, ListView):
    '''
    creates a list view for the recipe list
    '''
    context_object_name = "recipes"
    queryset = Recipe.objects.all()
    template_name = "recipes.html"

class RecipeDetailView(LoginRequiredMixin, DetailView):
    '''
    creates a detailed view for the recipes
    '''
    context_object_name = "recipe"
    model = Recipe
    template_name = "recipe.html"