from django.db import models

# Create your Book model here.
# Create Meta class inside the Book model

class Book(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    
    def __str__(self):
        return f"{self.title} (by: {self.author})"
    
    class Meta:
        indexes = models.Index(fields=['price']),
