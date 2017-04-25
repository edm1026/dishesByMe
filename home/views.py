from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from .forms import UserForm, RecipeForm
from django.db.models import Q
from .forms import RecipeForm
from .models import Recipe

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def search(request):
    try:
        recipe_ids = []
        for recipe in Recipe.objects.all():
            recipe_ids.append(recipe.pk)
        users_recipes = Recipe.objects.filter(pk__in=recipe_ids)
    except Recipe.DoesNotExist:
        users_recipes = []
    return render(request, 'home/recipe_list.html', {
        'recipe_list': users_recipes
    })


def index(request):
    recipes = Recipe.objects.all()
    query = request.GET.get("q")
    if query:
        recipes = recipes.filter(
            Q(recipeTitle__icontains=query)
        ).distinct()
        return render(request, 'home/searchResults.html', {
            'recipes': recipes
        })
    else:
        return render(request, 'home/searchResults.html', {'recipes': recipes})


def appetizer(request):
    recipes = Recipe.objects.all()
    query = request.GET.get("q")
    if query:
        recipes = recipes.filter(
            Q(recipeTitle__icontains=query)
        ).distinct()
        return render(request, 'home/appetizer.html', {
            'recipes': recipes
        })
    else:
        return render(request, 'home/appetizer.html', {'recipes': recipes})


def soup_salad(request):
    recipes = Recipe.objects.all()
    query = request.GET.get("q")
    if query:
        recipes = recipes.filter(
            Q(recipeTitle__icontains=query)
        ).distinct()
        return render(request, 'home/soupSalad.html', {
            'recipes': recipes
        })
    else:
        return render(request, 'home/soupSalad.html', {'recipes': recipes})


def entree(request):
    recipes = Recipe.objects.all()
    query = request.GET.get("q")
    if query:
        recipes = recipes.filter(
            Q(recipeTitle__icontains=query)
        ).distinct()
        return render(request, 'home/entree.html', {
            'recipes': recipes
        })
    else:
        return render(request, 'home/entree.html', {'recipes': recipes})


def dessert(request):
    recipes = Recipe.objects.all()
    query = request.GET.get("q")
    if query:
        recipes = recipes.filter(
            Q(recipeTitle__icontains=query)
        ).distinct()
        return render(request, 'home/dessert.html', {
            'recipes':recipes
        })
    else:
        return render(request, 'home/dessert.html', {'recipes': recipes})


def allRecipes(request):
    recipes = Recipe.objects.all()
    query = request.GET.get("q")
    if query:
        recipes = recipes.filter(
            Q(recipeTitle__icontains=query)
        ).distinct()
        return render(request, 'home/allRecipes.html', {
            'recipes': recipes
        })
    else:
        return render(request, 'home/allRecipes.html', {'recipes': recipes})


class TemplateView(generic.TemplateView):
    template_name = 'home/dishesByMeWelcome.html'


def detail(request, recipe_id):
    user = request.user
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'home/detail.html', {'recipe': recipe, 'user': user})


def createRecipe(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login_template.html')
    else:
        form = RecipeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.recipeImage = request.FILES['recipeImage']
            file_type = recipe.recipeImage.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'recipe': recipe, 'form':form, 'error_message': 'Image file must be PNG, JPG, or JPEG'
                }
                return render(request, 'home/recipe_form.html', context)
            recipe.save()
            return render(request, 'home/detail.html', {'recipe': recipe})
        context = {
            "form": form
        }
        return render(request, 'home/recipe_form.html', context)

def updateRecipe(request, recipe_id):
    if not request.user.is_authenticated():
        return render(request, 'home/login_template.html')
    else:
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        form = RecipeForm(request.POST or None, request.FILES or None, instance=recipe)
        if request.POST and form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            file_type = recipe.recipeImage.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'recipe': recipe, 'form': form, 'error_message': 'Image file must be PNG, JPG, or JPEG'
                }
                return render(request, 'home/recipe_form.html', context)
            recipe.save()
            return render(request, 'home/detail.html', {'recipe': recipe})
        context = {
            "form": form
        }
        return render(request, 'home/recipe_form.html', context)


def deleteRecipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    recipe.delete()
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'home/dishesByMeWelcome.html', {'recipes': recipes})


class UserFormView(View):
    form_class = UserForm
    template_name = 'home/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # register and add user to database
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # check info for validity
            # creates object from form..w/o saving to db
            user = form.save(commit=False)

            # normalized/formatted data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            # saves to db
            user.save()

            # returns User obj if credentials are valid
            user = authenticate(username=username, password=password)

            if user is not None:

                # you have ability to ban or disable user
                if user.is_active:
                    login(request, user)
                    return redirect('home:index')

        return render(request, self.template_name, {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # recipes = Recipe.objects.filter(user=request.user)
                recipes = Recipe.objects.all()
                return render(request, 'home/dishesByMeWelcome.html', {'recipes': recipes})
            else:
                return render(request, 'home/login_template.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'home/login_template.html', {'error_message': 'Invalid login'})
    return render(request, 'home/login_template.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {"form": form}
    return render(request, 'home/login_template.html', context)
