from django.db import models
import uuid
# Create your models here.
class Recipe(models.Model):
  name = models.CharField(max_length = 200,null = True,blank = True)  
  id = models.UUIDField(default = uuid.uuid4,editable = False,unique = True,primary_key = True)
  prep = models.TextField(null = True,blank  = True)

  def __str__(self):
    return self.name

class Ingredients(models.Model):
  ingredient = models.CharField(max_length = 200)
  recipe = models.ForeignKey(Recipe,on_delete = models.CASCADE)

  def __str__(self):
    return self.ingredient