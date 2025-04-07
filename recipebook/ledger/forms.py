from django import forms
from .models import Recipe, RecipeImage

# Form for creating a Recipe
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'author']  # Only include fields you want users to fill out

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Recipe Name'})
        self.fields['author'].widget.attrs.update({'class': 'form-control'})  # Author will be set automatically

# Form for uploading a Recipe Image
class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']  # Allow users to add an image and description

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Image Description'})
