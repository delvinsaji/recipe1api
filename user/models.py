from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from project.models import Recipe
import uuid
# Create your tests here.


class Profile(models.Model):
  name = models.CharField(max_length = 200,null  = True,blank = True)
  id = models.UUIDField(default = uuid.uuid4,editable = False,unique = True,primary_key = True)
  user = models.OneToOneField(User,on_delete = models.CASCADE,null = True,blank = True)
  email = models.EmailField(null = True,blank = True)

  def __str__(self):
    return self.name

class Reviews(models.Model):
  Rating = models.IntegerField(null = True,blank = True)
  desc = models.TextField(null = True,blank = True)
  recipe = models.ForeignKey(Recipe,on_delete = models.CASCADE)
  owner = models.ForeignKey(Profile,on_delete = models.CASCADE,null = True,blank  = True)

  def __str__(self):
    return self.recipe.name