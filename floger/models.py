from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/1.10/topics/db/models/
# https://docs.djangoproject.com/en/1.10/ref/models/fields/

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class Ingredient_amount(models.Model):
    AMOUNTS = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    ingredient = models.ForeignKey(Ingredient)
    amount = models.CharField(max_length=1, choices=AMOUNTS)
