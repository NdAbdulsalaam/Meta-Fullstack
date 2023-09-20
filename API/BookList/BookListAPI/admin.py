from django.contrib import admin
from .models import Book

my_models = [Book, ]
admin.site.register(my_models)