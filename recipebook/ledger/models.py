from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    '''
    creates profiles to allow for multiple users
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    '''
    used for the names of the ingredients
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[self.pk])

class Recipe(models.Model):
    '''
    used for the names of the recipes
    '''
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[self.pk])

class RecipeIngredient(models.Model):
    '''
    keeps the specific ingredients needed for specific recipes
    '''
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name="recipe"
        )
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name="ingredients"
        )
    
class RecipeImage(models.Model):
    '''
    used for the image and description of the recipes
    '''
    image = models.ImageField(upload_to='recipe_images/')
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe'
    )

    def __str__(self):
        return self.description
