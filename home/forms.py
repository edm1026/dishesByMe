from django.contrib.auth.models import User
from django import forms
from .models import Recipe

CTYPE = (
    ('N/A', 'N/A'),
    ('Lunch','Lunch'),
    ('Dinner','Dinner'),
    ('Lunch & Dinner','Lunch & Dinner'),
)
MTYPE = (
    ('Appetizer', 'Appetizer'),
    ('Soup & Salad', 'Soup & Salad'),
    ('Entree', 'Entree'),
    ('Dessert', 'Dessert'),
    ('Beverage', 'Beverage'),
)

class RecipeForm(forms.ModelForm):
     error_cs_class = 'error'

     # ctype = forms.ChoiceField(choices=CTYPE, required=True)
     # mtype = forms.ChoiceField(choices=MTYPE, required=True)

     class Meta:
         model = Recipe
         #fields = '__all__'
         #fields = ['user', 'recipeTitle','description', 'recipeImage', 'courseType', 'mealType', 'ingredients', 'directions']
         exclude = ['user', 'ctype', 'mtype']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    #^encrypt password

    # Meta is info about class
    class Meta:
        model = User
        fields = ['username', 'email', 'password']