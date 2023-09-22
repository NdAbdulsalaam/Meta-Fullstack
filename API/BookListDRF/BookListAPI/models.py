from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.title} (by: {self.author})"

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=225)
    
    def __str__(self) -> str:
        return self.title
    
class MenuItem(models.Model):
    title = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    
    def __str__(self) -> str:
        return self.title