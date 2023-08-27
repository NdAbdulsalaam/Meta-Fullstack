from django.db import models
# from django.utils import timezone

# Create your models here.
# class Members(models.Model):
#     MemberCat = (
#         ("1", "New"),
#         ("2", "Silver"),
#         ("3", "Gold"),
#         ("4", "Diamond")
#         )
    
#     MemberID = models.IntegerField(primary_key=True)
#     MemberType = models.CharField(max_length=12, choices=MemberCat, default='1')
#     FirstName = models.CharField(max_length=20)
#     LastName = models.CharField(max_length=20)
#     Email = models.EmailField(null=False, default="admin@gmail.com")
#     DateOfBirth = models.DateField()
#     Joined = models.DateTimeField(null=True)
    
#     class Meta:
#         db_table = "Members"

# class DrinksCategory(models.Model):
#     category_name = models.CharField(max_length = 200)
    
# class Drinks(models.Model):
#     drink = models.CharField(max_length = 200)
#     price = models.IntegerField()
#     category_id = models.ForeignKey(DrinksCategory, on_delete = models.PROTECT, default=None)
    

# class Booking(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     guest_count = models.IntegerField()
#     reservation_time = models.DateField(auto_now=True)
#     comments = models.CharField(max_length=1000)

class Employees(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    shift = models.IntegerField()
      
    def __str__(self):
        
        return f"{self.first_name} {self.last_name}"