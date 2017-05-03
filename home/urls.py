from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

#app_name = 'home'

urlpatterns = [
    # /home/
    # url(r'^RecipesHome/$', views.IndexView.as_view(), name='index'),
    url(r'^RecipesHome/$', views.index, name='index'),

    # /home/DishesByMe
    url(r'^dishesByMe/$', views.TemplateView.as_view(), name='dishesByMe'),

    # /home/Appetizer
    # url(r'^Appetizer/$', views.IndexView.as_view(), name='appetizer'),
    url(r'^Appetizer/$', views.appetizer, name='appetizer'),

    url(r'^Soups&Salads/$', views.soup_salad, name='soupSalad'),

    url(r'^Entrees/$', views.entree, name='entree'),

    url(r'^Desserts/$', views.dessert, name='dessert'),

    url(r'^allRecipes/$', views.allRecipes, name='allRecipes'),

    #url(r'^search/$', 'dishesByMe.home.views.search'),
    url(r'^search/$', views.search, name='search'),

    # #
     url(r'^login/$', views.login_user, name='login_user'),
    #
     url(r'^logout/$', views.logout_user, name= 'logout_user'),
    #
    # url(r'^admin/', admin.site.urls),
    #
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #/home/recipeId/
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<recipe_id>[0-9]+)/$', views.detail, name='detail'),

    # /home/recipe/add/
    # url(r'recipe/add/$', views.RecipeCreate.as_view(), name='recipe-add'),
    url(r'recipe/add/$', views.createRecipe, name='recipe-add'),

    # /home/recipe/2/
    # url(r'recipe/(?P<pk>[0-9]+)/update/$', views.RecipeUpdate.as_view(), name='recipe-update'),
    url(r'recipe/(?P<recipe_id>[0-9]+)/update/$', views.updateRecipe, name='recipe-update'),

    # /home/recipe/2/
    # url(r'recipe/(?P<pk>[0-9]+)/delete/$', views.RecipeDelete.as_view(), name='recipe-delete'),
    url(r'recipe/(?P<recipe_id>[0-9]+)/delete/$', views.deleteRecipe, name='recipe-delete'),

]

#def home(request):
#    return render(request,'home/dishesByMeWelcome.html')
