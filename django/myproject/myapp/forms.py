from django import forms
from .models import *

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = "__all__"

class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"