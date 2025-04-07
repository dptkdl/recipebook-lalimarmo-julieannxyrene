from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm

# List of Recipes
class RecipeListView(LoginRequiredMixin, ListView):
    context_object_name = "recipes"
    model = Recipe
    template_name = "recipes.html"

# Recipe Detail
class RecipeDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "recipe"
    model = Recipe
    template_name = "recipe.html"

# Create a Recipe
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_form.html"

    def form_valid(self, form):
        # Assign the currently logged-in user as the author
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('ledger:recipe-detail', args=[self.object.pk])

# Upload Recipe Image
class RecipeImageUploadView(LoginRequiredMixin, FormView):
    form_class = RecipeImageForm
    template_name = 'recipe_image_form.html'

    def form_valid(self, form):
        # Associate the image with the specific recipe
        recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        form.instance.recipe = recipe
        form.save()
        return redirect('ledger:recipe-detail', pk=recipe.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = Recipe.objects.get(pk=self.kwargs['pk'])
        return context
