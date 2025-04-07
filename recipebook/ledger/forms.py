from django import forms
from .models import Recipe, RecipeImage, RecipeIngredient, Ingredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name"]

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ["recipe", "ingredient", "quantity"]

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = "__all__"