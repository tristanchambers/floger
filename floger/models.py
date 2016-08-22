from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/1.10/topics/db/models/
# https://docs.djangoproject.com/en/1.10/ref/models/fields/
#
# Any time you edit this file you have to run:
# manage.py makemigrations
# manage.py migrate

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Flog(models.Model):
    date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return '%s' % (self.date)

class Ingredient_amount(models.Model):
    AMOUNTS = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    ingredient = models.ForeignKey(Ingredient)
    amount = models.CharField(max_length=1, choices=AMOUNTS)
    flog = models.ForeignKey(Flog)
    def __str__(self):
        return '%s %s' % (self.ingredient, self.amount)
