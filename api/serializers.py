from project.models import Recipe,Ingredients
from user.models import Profile,Reviews
from rest_framework import serializers

class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reviews
    fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
  my_reviews = serializers.SerializerMethodField("get_my_reviews")

  class Meta:
    model = Profile
    fields = "__all__"

  def get_my_reviews(self,profile):
    reviews = Reviews.objects.filter(owner = profile)
    serializer = ReviewSerializer(reviews,many = True)
    return serializer.data

class IngredientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ingredients
    fields = "__all__"

class RecipeSerializer(serializers.ModelSerializer):
  ingredients = serializers.SerializerMethodField('get_ingredients')
  reviews = serializers.SerializerMethodField("get_reviews")

  class Meta:
    model = Recipe
    fields = ["id","name","prep",'ingredients']

  def get_ingredients(self,rec):
    ingredients = Ingredients.objects.filter(recipe = rec)
    serializer = IngredientSerializer(ingredients,many = True)
    return serializer.data

  def get_reviews(self,rec):
    reviews = Reviews.objects.filter(recipe = rec)
    serializer = ReviewSerializer(reviews,many = True)
    return serializer.data
