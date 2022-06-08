from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import RecipeSerializer,ReviewSerializer
from project.models import Recipe,Ingredients
from user.models import Profile,Reviews
from rest_framework.response import Response
from django.contrib.auth.models import User

#All the CRUD functionalities
@api_view(['GET'])
def get_recipes(request):
  recipes = Recipe.objects.all()
  serializer = RecipeSerializer(recipes,many = True)
  return Response(serializer.data)




@api_view(['GET'])
def get_indi_recipe(request,pk):
  recipes = Recipe.objects.get(name = pk)
  serializer = RecipeSerializer(recipes,many = False)
  return Response(serializer.data)
# Create your views here.




@api_view(['POST'])
def create_recipe(request):
  if Recipe.objects.get(name = request.data['name']) is not None:
    return Response("The Recipe already exists")

  recipe = Recipe.objects.create(name = request.data['name'],prep = request.data['prep'])
  recipe.save()

  for items in request.data['ingredients']:
    ing = Ingredients.objects.create(ingredient = items,recipe = recipe)
    ing.save()
  
  return Response("Recipe created")




@api_view(['GET'])
def delete_recipe(request,pk):
  recipe = Recipe.objects.get(name = pk)
  ingredients = Ingredients.objects.filter(recipe = recipe)

  recipe.delete()
  ingredients.delete()

  return Response("Successfully deleted")




@api_view(['POST'])
def update_recipe(request,pk):
  recipe = Recipe.objects.get(name = pk)

  if request.data['name'] != "":
    recipe.name = request.data['name']
  if request.data['prep'] != "":
    recipe.prep = request.data['prep']
  recipe.save()

  if request.data['delete_ingredient'] != "":
    for items in request.data['delete_ingredient']:
      ingredient  = Ingredients.objects.get(ingredient = items)
      ingredient.delete()

  if request.data['create_ingredient'] != "":
    for items in request.data['create_ingredient']:
      ingredient = Ingredients.objects.create(ingredient = items,recipe = recipe)
      ingredient.save()
    
  return Response("Successfully updated")




@api_view(['GET'])
def search(request,pk):
  recipe = Recipe.objects.filter(name__icontains = pk)
  serializer = RecipeSerializer(recipe,many = True)
  return Response(serializer.data)



@api_view(['GET'])
def get_recipe_reviews(request,pk):
  reviews = Reviews.objects.filter(recipe = Recipe.objects.get(name = pk))
  serializer = ReviewSerializer(reviews,many = True)
  return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_review(request,pk):
  review = Reviews.objects.get(owner = Profile.objects.get(user = User.objects.get(username = request.data['username'])),
                                  recipe = Recipe.objects.get(name = pk))

  if review is not None:
    return Response("Review already exists")

  review = Reviews.objects.create(owner = Profile.objects.get(user = User.objects.get(username = request.data['username'])),
                                  recipe = Recipe.objects.get(name = pk),
                                  desc = request.data['desc'],
                                  Rating = request.data['rating'])
  review.save()
  return Response("Review added")




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_review(request,pk):
  review = Reviews.objects.get(owner = Profile.objects.get(user = User.objects.get(username = request.data['username'])),
                              recipe = Recipe.objects.get(name = pk))
  review.delete()
  return Response("Review deleted")


@api_view(['POST'])
def create_user(request):
  user = User.objects.get(username = request.data['username'])
  if user is not None:
    return Response("The user already exists")

  user = User.objects.create_user(username = request.data['username'])
  user.set_password(request.data['password'])
  user.save()

  profile = Profile.objects.create(name = request.data['name'],user = user)

  return Response("User created")