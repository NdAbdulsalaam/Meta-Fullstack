from django.db import models
# from django.utils import timezone

# Create your models here.
class Members(models.Model):
    MemberCat = (
        ("1", "New"),
        ("2", "Silver"),
        ("3", "Gold"),
        ("4", "Diamond")
        )
    
    MemberID = models.IntegerField(primary_key=True)
    MemberType = models.CharField(max_length=12, choices=MemberCat, default='1')
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Email = models.EmailField(null=False, default="admin@gmail.com")
    DateOfBirth = models.DateField()
    Joined = models.DateTimeField(null=True)
    
    class Meta:
        db_table = "Members"
    

    