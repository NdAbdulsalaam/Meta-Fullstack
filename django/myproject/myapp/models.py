from django.db import models
from django.utils import dates

# Create your models here.
class Members(models.Model):
    MemberID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    DateOfBirth = models.DateField()
    Joined = models.DateTimeField()
    

    