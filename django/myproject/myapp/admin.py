from django.contrib import admin
from .models import DrinksCategory, Drinks

# Register your models here.
admin.site.register(Drinks)
admin.site.register(DrinksCategory)