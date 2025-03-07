from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

# Register your models here.
class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

    list_display = ('name', )

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    list_display = ('name', )

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

    list_display = ('Quantity', 'Ingredient', 'Recipe', )

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)