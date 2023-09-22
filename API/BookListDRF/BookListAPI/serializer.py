from . import models
from rest_framework import serializers as seria

class BookSerializer(seria.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['id', 'title', 'author', 'price']
        
class MenuItemSerializer(seria.ModelSerializer):
    class Meta:
        model = models.MenuItem
        fields = ['id', 'title', 'price', 'inventory']
        
    extra_kwargs = {
        'price': {
            'min_value': 2
        },
        'inventory': {
            'min_value': 0
        }
    }
    
class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']