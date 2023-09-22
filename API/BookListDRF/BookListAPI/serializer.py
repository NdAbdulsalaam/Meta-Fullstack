from . import models
from rest_framework import serializers as seria

class BookSerializer(seria.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['id', 'title', 'author', 'price']
    
class CategorySerializer(seria.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id','title']
        
class MenuItemSerializer(seria.ModelSerializer):
    category_id = seria.IntegerField(write_only = True)
    category = CategorySerializer(read_only = True)
    class Meta:
        model = models.MenuItem
        fields = ['id', 'title', 'price', 'inventory', 'category', 'category_id']
        
    extra_kwargs = {
        'price': {
            'min_value': 2
        },
        'inventory': {
            'min_value': 0
        }
    }