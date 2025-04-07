from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeImage, RecipeIngredient, Ingredient
from .forms import RecipeForm, RecipeImageForm, RecipeIngredientForm, IngredientForm

class RecipeListView(LoginRequiredMixin, ListView):
    '''
    creates list view for recipe list
    '''
    context_object_name = "recipes"
    queryset = Recipe.objects.all()
    template_name = "recipes.html"

class RecipeDetailView(LoginRequiredMixin, DetailView):
    '''
    creates detailed view for the recipe
    '''
    context_object_name = "recipe"
    model = Recipe
    template_name = "recipe.html"
    extra = {"images":RecipeImage.objects.all}

class RecipeCreateView(LoginRequiredMixin, CreateView):
    '''
    creates view fpr new recipe form
    '''
    model = Recipe
    form_class = RecipeForm
    template_name = "recipe_form.html"
    success_url = "/recipe/add/recipeingredient/"

    def form_valid(self, form):
        # Assign the currently logged-in user as the author
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RecipeCreateView, self).get_context_data(**kwargs)
        context['recipe_form']=context['form']
        return context

# Upload Recipe Image
class RecipeIngredientCreateView(LoginRequiredMixin, CreateView):
    '''
    creates view for recipe ingredient of recipe detail form
    '''
    form_class = RecipeIngredientForm
    template_name = 'recipeingredient_form.html'
    model = RecipeIngredient
    success_url = reverse_lazy('ledger:recipes-list')

    def get_context_data(self, **kwargs):
        context = super(RecipeIngredientCreateView).get_context_data(**kwargs)
        context['recipeingredient_form'] = context['form']
        return context

class IngredientCreateView(LoginRequiredMixin, CreateView):
    '''
    creates view for new ingredient form
    '''
    form_class = IngredientForm
    template_name = 'ingredient_form.html'
    model = Ingredient
    success_url = 'recipe/add/recipeingredient'

    def get_context_data(self, **kwargs):
        context = super(IngredientCreateView, self).get_context_data(**kwargs)
        context['ingredient_form'] = context['form']
        return context
    
class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    '''
    creates view for new recipe image form
    '''
    model = RecipeImage
    template_name = 'recipeimage_form.html'
    form_class = RecipeImageForm

    def get_success_url(self):
        return reverse_lazy('legder:recipe-detail', kwargs={ 'pk':self.object.recipe.pk})
    
    def get_context_data(self, **kwargs):
        context = super(RecipeImageCreateView, self).get_context_data(**kwargs)
        context['recipeimage_form'] = context['form']
        return context