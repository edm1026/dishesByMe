from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here. where the data 4 the classes on this page will go
#classes go here

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
)

#pk/id 1
class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    recipeTitle = models.CharField(max_length=150)
    description = models.TextField(max_length=20000)
    recipeImage = models.FileField()
    courseType = models.CharField(max_length=14, choices=CTYPE)
    mealType = models.CharField(max_length=15, choices=MTYPE)
    ingredients = models.TextField(max_length=20000)
    directions = models.TextField(max_length=10000)

    def get_absolute_url(self):
        return reverse('home:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.recipeTitle + " - " + self.mealType + " - " + self.courseType
