from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Ingredient, Recipe, RecipeIngredient, Profile, RecipeImage

class IngredientAdmin(admin.ModelAdmin):
    '''
    creates the admin panel for the Ingredient model
    '''
    model = Ingredient
    list_display = ('name', )

class RecipeIngredientInline(admin.TabularInline):
    '''
    creates the admin panel for the RecipeIngredient model
    '''
    model = RecipeIngredient
    list_display = ('quantity', 'ingredient', 'recipe', )

class RecipeImageInline(admin.StackedInline):
    '''
    creates admin panel for RecipeImage model
    '''
    model = RecipeImage

class RecipeAdmin(admin.ModelAdmin):
    '''
    creates the admin panel for the Recipe model
    '''
    model = Recipe
    list_display = ('name', )
    inlines = [RecipeImageInline, RecipeIngredientInline]


class ProfileInline(admin.StackedInline):
    '''
    makes sure that the Profile model is with the User model
    '''
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    '''
    adds Profile model to the User panel
    '''
    inlines = [ProfileInline,]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)