from . import models
from rest_framework import serializers as seria

class BookSerializer(seria.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['id', 'title', 'author', 'price']