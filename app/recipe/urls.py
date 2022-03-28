from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views

# The default router is a feature of the djngo rest_framework that will
# auto generate the urls for our viewsets. you may have multiple urls associated
# with one viewset

router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('Ingredient', views.IngredientViewSet)
router.register('recipes', views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
