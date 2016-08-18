from django.contrib import admin
from .models import Ingredient
from .models import Ingredient_amount
from .models import Flog

# Register your models here.
# https://docs.djangoproject.com/en/1.10/ref/contrib/admin/

admin.site.register(Ingredient)

class Ingredient_amountInline(admin.TabularInline):
    model = Ingredient_amount

class FlogAdmin(admin.ModelAdmin):
    inlines = [
        Ingredient_amountInline,
    ]

admin.site.register(Flog, FlogAdmin)
