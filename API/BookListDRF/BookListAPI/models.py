from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.title} (by: {self.author})"

class MenuItem(models.Model):
    title = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()